"""
GameClips AI - Local Flask Backend Application
Phase 1: Multi-Game Core Dashboard, SQLite Engine, and Storage Management
"""

import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
from database import get_connection, init_database
from storage_manager import get_disk_status, cleanup_temporary_files
from research_agent import run_research_cycle, get_topic_evidence_report
from footage_agent import populate_initial_footage_catalog, verify_asset_rights, search_assets_for_topic
from script_generator import generate_script_for_topic
from visual_engine import render_scene_frame, generate_visuals_for_project
from video_engine import render_video_project
from verification_engine import verify_project_compliance, record_approval_decision
from export_manager import export_approved_project, list_all_exports, get_export_by_id
from analytics_engine import get_analytics_summary
from scheduler import get_scheduler_status, run_automation_cycle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp_render")
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Ensure database is initialized on startup
init_database()

@app.route("/")
def index():
    """Serves the main local dashboard UI."""
    return render_template("index.html")

@app.route("/api/health")
def health():
    """Simple health check endpoint."""
    return jsonify({
        "status": "healthy",
        "app": "GameClips AI",
        "version": "1.0.0-phase1",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/stats")
def get_stats():
    """Returns aggregated stats for dashboard cards."""
    conn = get_connection()
    cur = conn.cursor()

    # Active game
    cur.execute("SELECT * FROM games WHERE is_active = 1 LIMIT 1")
    active_game_row = cur.fetchone()
    active_game = dict(active_game_row) if active_game_row else None

    # Topics count
    cur.execute("SELECT COUNT(*) FROM topics")
    topics_count = cur.fetchone()[0]

    # Scripts count
    cur.execute("SELECT COUNT(*) FROM scripts")
    scripts_count = cur.fetchone()[0]

    # Approval queue count (PENDING or NEEDS_REVIEW)
    cur.execute("SELECT COUNT(*) FROM video_projects WHERE status IN ('PENDING', 'NEEDS_REVIEW')")
    awaiting_approval_count = cur.fetchone()[0]

    # Exported videos count
    cur.execute("SELECT COUNT(*) FROM exported_videos")
    exported_count = cur.fetchone()[0]

    # Rejected assets count
    cur.execute("SELECT COUNT(*) FROM footage_assets WHERE rights_status = 'REJECTED'")
    rejected_assets_count = cur.fetchone()[0]

    conn.close()

    # Storage metrics
    storage_info = get_disk_status()

    return jsonify({
        "active_game": active_game,
        "topics_count": topics_count,
        "scripts_count": scripts_count,
        "awaiting_approval_count": awaiting_approval_count,
        "exported_count": exported_count,
        "rejected_assets_count": rejected_assets_count,
        "storage": storage_info
    })

@app.route("/api/games", methods=["GET"])
def list_games():
    """Lists all games in the modular game library."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM games ORDER BY is_active DESC, name ASC")
    games = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(games)

@app.route("/api/games/<game_id>/activate", methods=["POST"])
def activate_game(game_id):
    """Activates the specified game and deactivates all others."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE games SET is_active = 0")
    cur.execute("UPDATE games SET is_active = 1, updated_at = ? WHERE id = ?", (datetime.now().isoformat(), game_id))
    cur.execute("SELECT name FROM games WHERE id = ?", (game_id,))
    row = cur.fetchone()
    conn.commit()
    conn.close()

    if row:
        return jsonify({"success": True, "game_name": row["name"]})
    return jsonify({"success": False, "error": "Game not found"}), 404

@app.route("/api/games/add", methods=["POST"])
def add_game():
    """Adds a new game to the library with full policy and footage configurations."""
    data = request.get_json(silent=True) or {}
    name = data.get("name", "").strip()
    if not name:
        return jsonify({"success": False, "error": "Game name is required"}), 400

    slug = name.lower().replace(" ", "-").replace(":", "").replace("'", "")
    game_id = f"game-{slug[:16]}"
    now = datetime.now().isoformat()

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name FROM games WHERE name = ? OR slug = ?", (name, slug))
        existing = cur.fetchone()
        if existing:
            conn.close()
            return jsonify({"success": True, "game_id": existing["id"], "name": existing["name"], "message": "Game already exists in library."})

        cur.execute("""
        INSERT INTO games (
            id, name, slug, description, developer, publisher, official_sources,
            fan_content_policy_url, commercial_rules, approved_footage_sources,
            restricted_rules, supported_categories, research_config, is_active,
            created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
        """, (
            game_id,
            name,
            slug,
            data.get("description", f"Content library for {name}"),
            data.get("developer", "Unknown"),
            data.get("publisher", "Unknown"),
            json.dumps([data.get("official_sources")] if data.get("official_sources") else []),
            data.get("fan_content_policy_url", ""),
            data.get("commercial_rules", "Verify specific game fan content policy before publishing."),
            json.dumps([data.get("approved_footage_sources", "Original SVG/CSS Visuals")]),
            json.dumps([data.get("restricted_rules", "No leaked footage.")]),
            json.dumps(["Facts & Secrets", "Cars & Comparisons", "Stories", "Mechanics"]),
            json.dumps({"search_keywords": [name]}),
            now,
            now
        ))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "game_id": game_id, "name": name})
    except Exception as e:
        conn.close()
        return jsonify({"success": False, "error": str(e)}), 400

@app.route("/api/topics", methods=["GET"])
def get_topics():
    """Gets research topics for the active game."""
    conn = get_connection()
    cur = conn.cursor()
    # Get active game id
    cur.execute("SELECT id FROM games WHERE is_active = 1 LIMIT 1")
    active_row = cur.fetchone()
    game_id = active_row["id"] if active_row else None

    if game_id:
        cur.execute("""
        SELECT t.*, (SELECT COUNT(*) FROM research_sources s WHERE s.topic_id = t.id) as source_count
        FROM topics t
        WHERE t.game_id = ?
        ORDER BY t.relevance_score DESC, t.created_at DESC
        """, (game_id,))
    else:
        cur.execute("SELECT *, 0 as source_count FROM topics ORDER BY relevance_score DESC")

    topics = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(topics)

@app.route("/api/topics", methods=["POST"])
def add_topic():
    """Adds a new topic to the active game."""
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"success": False, "error": "Topic title is required"}), 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM games WHERE is_active = 1 LIMIT 1")
    active_row = cur.fetchone()
    if not active_row:
        conn.close()
        return jsonify({"success": False, "error": "No active game selected"}), 400

    game_id = active_row["id"]
    now = datetime.now().isoformat()
    topic_id = f"top-{int(datetime.now().timestamp())}"

    cur.execute("""
    INSERT INTO topics (id, game_id, category, title, description, relevance_score, status, is_duplicate, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, 'DISCOVERED', 0, ?, ?)
    """, (
        topic_id,
        game_id,
        data.get("category", "Facts & Secrets"),
        title,
        data.get("description", ""),
        float(data.get("relevance_score", 8.0)),
        now,
        now
    ))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "topic_id": topic_id})

@app.route("/api/storage", methods=["GET"])
def get_storage():
    """Returns disk and storage metrics."""
    return jsonify(get_disk_status())

@app.route("/api/storage/cleanup", methods=["POST"])
def trigger_cleanup():
    """Cleans up temporary render files."""
    res = cleanup_temporary_files(force_all=True)
    return jsonify(res)

@app.route("/api/settings", methods=["GET"])
def get_settings():
    """Returns system settings and storage info."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT key, value FROM system_settings")
    settings = dict(cur.fetchall())
    conn.close()
    return jsonify({
        "settings": settings,
        "storage": get_disk_status()
    })

@app.route("/api/settings", methods=["POST"])
def update_settings():
    """Updates system settings in SQLite."""
    data = request.get_json(silent=True) or {}
    conn = get_connection()
    cur = conn.cursor()
    now = datetime.now().isoformat()

    for k, v in data.items():
        cur.execute("""
        INSERT INTO system_settings (key, value, updated_at)
        VALUES (?, ?, ?)
        ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
        """, (k, str(v), now))

    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route("/api/queue", methods=["GET"])
def get_approval_queue():
    """Lists video projects awaiting human approval with full rights and verification reports."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        SELECT p.*, s.title as script_title, s.hook, s.voiceover_text,
               s.youtube_title, s.youtube_description, s.tiktok_caption, s.hashtags,
               s.topic_id, g.name as game_name,
               v.status as vrf_status, v.copyright_risk_level, v.warning_notes, v.disclaimer_notice
        FROM video_projects p
        JOIN scripts s ON p.script_id = s.id
        JOIN games g ON p.game_id = g.id
        LEFT JOIN verification_reports v ON p.id = v.project_id
        WHERE p.status IN ('PENDING', 'NEEDS_REVIEW')
        ORDER BY p.created_at DESC
        """)
        rows = [dict(row) for row in cur.fetchall()]

        # Enhance each project with sources
        queue = []
        for r in rows:
            topic_id = r.get("topic_id")
            cur.execute("SELECT title, url, source_name FROM research_sources WHERE topic_id = ?", (topic_id,))
            sources = [dict(s) for s in cur.fetchall()]
            r["sources"] = sources
            queue.append(r)
        return jsonify(queue)
    finally:
        conn.close()

@app.route("/api/approval/<project_id>/action", methods=["POST"])
def handle_approval_action(project_id):
    """Processes human reviewer decisions: APPROVE, REJECT, or REGENERATE."""
    data = request.get_json(silent=True) or {}
    action = data.get("action", "").upper()
    reviewer_notes = data.get("reviewer_notes", "")
    warning_ack = data.get("warning_acknowledged", True)

    res = record_approval_decision(
        project_id=project_id,
        action=action,
        reviewer_notes=reviewer_notes,
        warning_acknowledged=warning_ack
    )
    if not res.get("success"):
        return jsonify(res), 400
    return jsonify(res)

@app.route("/api/approval/<project_id>/verify", methods=["POST"])
def trigger_project_verification(project_id):
    """Runs a complete 8-point compliance check on demand."""
    report = verify_project_compliance(project_id)
    return jsonify(report)

@app.route("/api/approval/<project_id>/metadata", methods=["POST"])
def update_project_metadata(project_id):
    """Allows human reviewer to edit publishing metadata before sign-off."""
    data = request.get_json(silent=True) or {}
    yt_title = data.get("youtube_title")
    yt_desc = data.get("youtube_description")
    tt_caption = data.get("tiktok_caption")
    hashtags = data.get("hashtags")

    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT script_id FROM video_projects WHERE id = ?", (project_id,))
        p_row = cur.fetchone()
        if not p_row:
            return jsonify({"success": False, "error": "Project not found"}), 404

        script_id = p_row["script_id"]
        cur.execute("""
        UPDATE scripts SET
            youtube_title = COALESCE(?, youtube_title),
            youtube_description = COALESCE(?, youtube_description),
            tiktok_caption = COALESCE(?, tiktok_caption),
            hashtags = COALESCE(?, hashtags)
        WHERE id = ?
        """, (yt_title, yt_desc, tt_caption, hashtags, script_id))
        conn.commit()
        return jsonify({"success": True, "message": "Metadata updated successfully."})
    finally:
        conn.close()

# --- PHASE 6: EXPORT CENTER, ANALYTICS & AUTOMATION ENDPOINTS ---

@app.route("/api/export/<project_id>", methods=["POST"])
def export_project(project_id):
    """Packages an approved project into release directory."""
    data = request.get_json(silent=True) or {}
    force = data.get("force", False)
    result = export_approved_project(project_id, force_export=force)
    status_code = 200 if result.get("success") else 400
    return jsonify(result), status_code

@app.route("/api/exports", methods=["GET"])
def get_exports():
    """Lists exported video packages with full metadata."""
    exports = list_all_exports()
    return jsonify(exports)

@app.route("/api/exports/<export_id>", methods=["GET"])
def get_export_details(export_id):
    """Fetches details for a single export package."""
    item = get_export_by_id(export_id)
    if not item:
        return jsonify({"success": False, "error": "Export package not found."}), 404
    return jsonify(item)

@app.route("/api/exports/<export_id>/file/<path:subpath>", methods=["GET"])
def get_export_file(export_id, subpath):
    """Streams or serves a specific file from an export package."""
    item = get_export_by_id(export_id)
    if not item or not item.get("export_folder"):
        return jsonify({"error": "Export not found"}), 404
    
    file_path = os.path.join(item["export_folder"], subpath)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found in package"}), 404

    as_attachment = request.args.get("download", "false").lower() == "true"
    return send_file(file_path, as_attachment=as_attachment)

@app.route("/api/analytics", methods=["GET"])
def get_analytics():
    """Returns aggregated channel and production metrics."""
    data = get_analytics_summary()
    return jsonify(data)

@app.route("/api/automation/status", methods=["GET"])
def get_automation_status():
    """Returns scheduler configuration, remaining quota, and hardware health."""
    data = get_scheduler_status()
    return jsonify(data)

@app.route("/api/automation/run", methods=["POST"])
def trigger_automation_run():
    """Triggers an automated candidate production cycle."""
    data = request.get_json(silent=True) or {}
    game_id = data.get("game_id")
    max_candidates = data.get("max_candidates")
    result = run_automation_cycle(game_id=game_id, max_candidates=max_candidates)
    return jsonify(result)

# --- PHASE 2: RESEARCH & FOOTAGE AGENT ENDPOINTS ---

@app.route("/api/research/run", methods=["POST"])
def trigger_research():
    """Executes a research cycle for the active game."""
    data = request.get_json(silent=True) or {}
    game_id = data.get("game_id")
    result = run_research_cycle(game_id)
    return jsonify(result)

@app.route("/api/research/topic/<topic_id>/evidence", methods=["GET"])
def get_topic_evidence(topic_id):
    """Retrieves full source citations and verified claims for a topic."""
    report = get_topic_evidence_report(topic_id)
    if not report:
        return jsonify({"success": False, "error": "Topic not found"}), 404
    return jsonify({"success": True, "report": report})

@app.route("/api/footage", methods=["GET"])
def list_footage():
    """Lists all assets with license audit details."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT a.*, l.attribution_notice, l.can_commercial, l.can_modify, l.verifier_notes
    FROM footage_assets a
    LEFT JOIN asset_licenses l ON a.id = l.asset_id
    ORDER BY a.download_date DESC
    """)
    assets = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(assets)

@app.route("/api/footage/search", methods=["GET", "POST"])
def search_footage():
    """Searches rights-verified assets matching topic keywords or query string."""
    from footage_agent import search_assets_for_topic
    import re
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        query = data.get("query", "")
        game_id = data.get("game_id")
    else:
        query = request.args.get("q", "")
        game_id = request.args.get("game_id")

    keywords = [k.strip() for k in re.split(r"[\s,;]+", query) if k.strip()] if query else []
    results = search_assets_for_topic(keywords, game_id=game_id)
    return jsonify({"success": True, "results": results, "count": len(results)})

@app.route("/api/footage/<asset_id>/download", methods=["POST"])
def download_footage_endpoint(asset_id):
    """Downloads or caches a permitted commercial footage asset into local library."""
    from footage_agent import download_permitted_asset
    result = download_permitted_asset(asset_id)
    if not result.get("success"):
        return jsonify(result), 400
    return jsonify(result)

@app.route("/api/footage/seed", methods=["POST"])
def seed_footage():
    """Seeds verified initial footage assets for the active game."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM games WHERE is_active = 1 LIMIT 1")
    row = cur.fetchone()
    conn.close()
    active_game_id = row["id"] if row else "game-gta6"
    res = populate_initial_footage_catalog(active_game_id)
    return jsonify({"success": True, **res})

@app.route("/api/footage/verify", methods=["POST"])
def audit_footage_license():
    """Audits an asset's commercial use rights and copyright risks."""
    data = request.get_json(silent=True) or {}
    audit = verify_asset_rights(data)
    return jsonify({"success": True, "audit": audit})

@app.route("/api/footage/add", methods=["POST"])
def add_footage_asset():
    """Records a new footage asset with full license traceability."""
    data = request.get_json(silent=True) or {}
    asset_name = data.get("asset_name", "").strip()
    source_platform = data.get("source_platform", "Unknown")
    source_url = data.get("source_url", "").strip()
    license_name = data.get("license_name", "").strip()

    if not asset_name or not source_url:
        return jsonify({"success": False, "error": "Asset name and Source URL are required."}), 400

    audit = verify_asset_rights(data)
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM games WHERE is_active = 1 LIMIT 1")
    active_row = cur.fetchone()
    game_id = active_row["id"] if active_row else "game-gta6"
    now = datetime.now().isoformat()
    asset_id = f"ast-user-{int(datetime.now().timestamp())}"

    cur.execute("""
    INSERT INTO footage_assets (
        id, game_id, asset_name, source_platform, source_url, asset_url,
        author_name, license_name, license_url, commercial_permission,
        attribution_required, rights_status, file_size_mb, download_date
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0.0, ?)
    """, (
        asset_id, game_id, asset_name, source_platform, source_url,
        data.get("asset_url", source_url), data.get("author_name", "Unknown"),
        license_name, data.get("license_url", ""), 1 if data.get("commercial_permission") else 0,
        1 if data.get("attribution_required") else 0, audit["rights_status"], now
    ))

    # Add license entry
    lic_id = f"lic-{asset_id}"
    cur.execute("""
    INSERT INTO asset_licenses (
        id, asset_id, license_name, license_text, can_commercial, can_modify,
        attribution_notice, verified_at, verifier_notes
    ) VALUES (?, ?, ?, ?, ?, 1, ?, ?, ?)
    """, (
        lic_id, asset_id, license_name, data.get("attribution_notice", ""),
        1 if data.get("commercial_permission") else 0, data.get("attribution_notice", ""),
        now, audit["notes"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"success": True, "asset_id": asset_id, "rights_status": audit["rights_status"], "audit": audit})

# --- PHASE 3: SCRIPT GENERATOR & VISUAL ENGINE ENDPOINTS ---

@app.route("/api/scripts", methods=["GET"])
def list_scripts():
    """Lists all generated scripts."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT s.*, g.name as game_name
    FROM scripts s
    JOIN games g ON s.game_id = g.id
    ORDER BY s.created_at DESC
    """)
    scripts = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(scripts)

@app.route("/api/studio/generate", methods=["POST"])
def studio_generate():
    """Generates a script, visual plan, and continuous-motion scenes in HYBRID MODE."""
    data = request.get_json(silent=True) or {}
    topic_id = data.get("topic_id")
    target_duration = data.get("target_duration", "45-60s")

    if not topic_id:
        return jsonify({"success": False, "error": "Please select a target topic."}), 400

    # 1. Generate Script & Scene Plan (Default: 45-60s)
    script_res = generate_script_for_topic(topic_id, target_duration)
    if not script_res.get("success"):
        return jsonify(script_res), 400

    project_id = script_res["project_id"]

    # 2. Generate Hybrid Visual Scenes (Authentic Gameplay + Realistic Moving Simulation)
    visual_res = generate_visuals_for_project(project_id, hybrid_mode=True)

    return jsonify({
        "success": True,
        "script": script_res,
        "visuals": visual_res,
        "project_id": project_id,
        "mode": "HYBRID"
    })

@app.route("/api/studio/project/<project_id>", methods=["GET"])
def get_project_details(project_id):
    """Retrieves full project details, scenes, and generated visual frames."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM video_projects WHERE id = ?", (project_id,))
    p_row = cur.fetchone()
    if not p_row:
        conn.close()
        return jsonify({"success": False, "error": "Project not found"}), 404

    project = dict(p_row)

    cur.execute("SELECT * FROM scripts WHERE id = ?", (project["script_id"],))
    s_row = cur.fetchone()
    script = dict(s_row) if s_row else None

    cur.execute("SELECT * FROM video_scenes WHERE project_id = ? ORDER BY scene_number ASC", (project_id,))
    scenes = [dict(r) for r in cur.fetchall()]
    conn.close()

    return jsonify({
        "success": True,
        "project": project,
        "script": script,
        "scenes": scenes
    })

@app.route("/api/preview/image/<project_id>/<int:scene_num>", methods=["GET"])
def get_preview_image(project_id, scene_num):
    """Serves the generated PNG frame for live visual preview in the browser."""
    frame_path = os.path.join(TEMP_DIR, "visuals", project_id, f"scene_{scene_num}.png")
    if os.path.isfile(frame_path):
        return send_file(frame_path, mimetype="image/png")
    return jsonify({"error": "Preview frame not found"}), 404

# --- PHASE 4: VIDEO RENDERING & STREAMING ENDPOINTS ---

@app.route("/api/video/render", methods=["POST"])
def video_render():
    """Renders a preview or final video candidate using FFmpeg."""
    data = request.get_json(silent=True) or {}
    project_id = data.get("project_id")
    is_preview = data.get("is_preview", False)
    quality_preset = data.get("quality_preset", "ultrafast")
    voice_name = data.get("voice_name", "Microsoft David Desktop")
    custom_audio_path = data.get("custom_audio_path")

    if not project_id:
        return jsonify({"success": False, "error": "project_id is required."}), 400

    res = render_video_project(
        project_id=project_id,
        is_preview=is_preview,
        quality_preset=quality_preset,
        voice_name=voice_name,
        custom_audio_path=custom_audio_path
    )

    if not res.get("success"):
        return jsonify(res), 400

    return jsonify(res)

@app.route("/api/video/stream/<project_id>", methods=["GET"])
def stream_video(project_id):
    """Streams the rendered MP4 video for HTML5 playback in the dashboard."""
    # Check final then preview
    final_path = os.path.join(TEMP_DIR, "projects", project_id, "final.mp4")
    preview_path = os.path.join(TEMP_DIR, "projects", project_id, "preview.mp4")

    target = None
    if os.path.isfile(final_path):
        target = final_path
    elif os.path.isfile(preview_path):
        target = preview_path

    if target:
        return send_file(target, mimetype="video/mp4", conditional=True)
    return jsonify({"error": "Video file not found or not rendered yet."}), 404

if __name__ == "__main__":
    print("=" * 50)
    print("  GameClips AI - Local Server Starting")
    print("  URL: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(host="127.0.0.1", port=5000, debug=False)
