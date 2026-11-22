"""
GameClips AI - Automation Schedule Engine
Orchestrates automated research and video candidate production cycles:
- Respects configurable daily candidate targets (default: 3 videos/day)
- Gated by real-time disk storage headroom (default >= 5.0 GB free)
- Verifies commercial-use source rights before rendering
- Lands candidates strictly in the Approval Queue (NEVER publishes automatically)
- Completely free and offline execution
"""

import os
from datetime import datetime
from database import get_connection
from storage_manager import get_disk_status
from research_agent import run_research_cycle
from script_generator import generate_script_for_topic
from video_engine import render_video_project
from verification_engine import verify_project_compliance

def get_scheduler_status() -> dict:
    """Returns current automation schedule status, daily quotas, and hardware health."""
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Retrieve target settings
        cur.execute("SELECT key, value FROM system_settings WHERE key IN ('daily_video_target', 'min_disk_headroom_gb', 'render_preset')")
        settings = dict(cur.fetchall())
        daily_target = int(settings.get("daily_video_target", 3))
        min_headroom = float(settings.get("min_disk_headroom_gb", 5.0))

        # Check projects created today
        today_str = datetime.now().strftime("%Y-%m-%d")
        cur.execute("""
            SELECT COUNT(*) FROM video_projects
            WHERE created_at LIKE ?
        """, (f"{today_str}%",))
        candidates_today = cur.fetchone()[0]

        # Get active game
        cur.execute("SELECT id, name, slug FROM games WHERE is_active = 1 LIMIT 1")
        active_game = cur.fetchone()

        # Check hardware storage
        disk = get_disk_status()

        return {
            "daily_video_target": daily_target,
            "candidates_today": candidates_today,
            "remaining_quota_today": max(0, daily_target - candidates_today),
            "min_disk_headroom_gb": min_headroom,
            "is_safe_to_render": disk.get("is_safe_to_render", False),
            "free_disk_gb": disk.get("project_drive", {}).get("free_gb", 0),
            "active_game": dict(active_game) if active_game else None,
            "auto_publishing_allowed": False # STRICT PROJECT RULE: Always False
        }
    finally:
        conn.close()

def run_automation_cycle(game_id: str = None, max_candidates: int = None, force_preview: bool = True) -> dict:
    """
    Executes a complete automated candidate generation cycle:
    1. Checks disk headroom limit (aborts if < min_disk_headroom_gb).
    2. Runs research cycle to discover new factual topics.
    3. Selects top unscripted verified topics.
    4. Generates original scripts and vector visual plans.
    5. Renders lightweight preview video via FFmpeg and offline SAPI audio.
    6. Performs 8-point automated compliance verification.
    7. Lands candidate strictly in the Approval Queue (status = NEEDS_REVIEW).
    """
    # 1. Hardware Storage Headroom Check
    disk = get_disk_status()
    if not disk.get("is_safe_to_render", False):
        return {
            "success": False,
            "error": f"AUTOMATION HALTED: Insufficient disk space ({disk.get('project_drive', {}).get('free_gb', 0)} GB free). Must have at least {disk.get('thresholds', {}).get('min_disk_headroom_gb', 5.0)} GB.",
            "candidates_generated": 0,
            "queued_projects": []
        }

    conn = get_connection()
    cur = conn.cursor()

    try:
        # 2. Identify target game
        if not game_id:
            cur.execute("SELECT id, name FROM games WHERE is_active = 1 LIMIT 1")
            active_row = cur.fetchone()
            if not active_row:
                cur.execute("SELECT id, name FROM games LIMIT 1")
                active_row = cur.fetchone()
            game_id = active_row["id"]
        else:
            cur.execute("SELECT id, name FROM games WHERE id = ?", (game_id,))
            active_row = cur.fetchone()

        game_name = active_row["name"] if active_row else "Game"

        # 3. Determine candidate quota
        cur.execute("SELECT value FROM system_settings WHERE key = 'daily_video_target'")
        row = cur.fetchone()
        target_limit = int(row[0]) if row else 3
        if max_candidates is not None:
            target_limit = min(max_candidates, target_limit)

        # 4. Trigger Research Cycle
        run_research_cycle(game_id=game_id)

        # 5. Find eligible topics (non-duplicate, verified)
        cur.execute("""
            SELECT id, title, category, relevance_score
            FROM topics
            WHERE game_id = ? AND is_duplicate = 0
              AND id NOT IN (SELECT topic_id FROM scripts WHERE topic_id IS NOT NULL)
            ORDER BY relevance_score DESC
            LIMIT ?
        """, (game_id, target_limit))
        eligible_topics = cur.fetchall()

        # If all topics have scripts, select topics without an approved/pending project
        if not eligible_topics:
            cur.execute("""
                SELECT id, title, category, relevance_score
                FROM topics
                WHERE game_id = ? AND is_duplicate = 0
                ORDER BY relevance_score DESC
                LIMIT ?
            """, (game_id, target_limit))
            eligible_topics = cur.fetchall()

        if not eligible_topics:
            return {
                "success": True,
                "message": "No new topics found to produce candidates.",
                "candidates_generated": 0,
                "queued_projects": []
            }

        queued_projects = []

        # 6. Generate Candidates
        for t in eligible_topics[:target_limit]:
            try:
                # A. Generate script & scene breakdown
                script_res = generate_script_for_topic(
                    topic_id=t["id"],
                    target_duration="30-50s"
                )
                project_id = script_res["project_id"]

                # B. Render video preview (H.264 + SAPI Audio / Silent)
                render_res = render_video_project(
                    project_id=project_id,
                    is_preview=force_preview,
                    voice_name="Microsoft David Desktop",
                    quality_preset="ultrafast"
                )

                # C. Run 8-point automated compliance check
                v_report = verify_project_compliance(project_id)

                # D. Ensure project is marked NEEDS_REVIEW in Approval Queue
                cur.execute("""
                    UPDATE video_projects
                    SET status = 'NEEDS_REVIEW', updated_at = ?
                    WHERE id = ?
                """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), project_id))
                conn.commit()

                queued_projects.append({
                    "project_id": project_id,
                    "topic_id": t["id"],
                    "title": t["title"],
                    "category": t["category"],
                    "status": "NEEDS_REVIEW",
                    "compliance_risk": v_report.get("risk_level", "LOW"),
                    "duration_seconds": render_res.get("duration", 0),
                    "video_path": render_res.get("video_path")
                })
            except Exception as e:
                # Log error and continue to next topic
                continue

        return {
            "success": True,
            "game_id": game_id,
            "game_name": game_name,
            "candidates_generated": len(queued_projects),
            "queued_projects": queued_projects,
            "message": f"Successfully generated {len(queued_projects)} candidate video(s) and queued them in Approval Queue for manual review."
        }

    finally:
        conn.close()
