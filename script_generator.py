"""
GameClips AI - Script Generator Engine
Generates original, high-retention short-form video scripts (30-50s and 60-90s)
with scene-by-scene visual plans, subtitles, and publishing metadata.
"""

import os
import json
import random
from datetime import datetime
from database import get_connection

def generate_script_for_topic(topic_id, target_duration="30-50s", game_id=None):
    """
    Generates an original video script, scene plan, subtitles, and metadata
    for a chosen topic.
    """
    conn = get_connection()
    cur = conn.cursor()

    # 1. Fetch topic & active game
    cur.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    t_row = cur.fetchone()
    if not t_row:
        conn.close()
        return {"success": False, "error": "Topic not found."}

    topic = dict(t_row)
    actual_game_id = game_id or topic["game_id"]

    cur.execute("SELECT * FROM games WHERE id = ?", (actual_game_id,))
    g_row = cur.fetchone()
    game = dict(g_row) if g_row else {"name": "Gaming", "slug": "gaming"}

    # 2. Fetch verified claims & sources for evidence incorporation
    cur.execute("SELECT * FROM factual_claims WHERE topic_id = ?", (topic_id,))
    claims = [dict(r) for r in cur.fetchall()]

    cur.execute("SELECT * FROM research_sources WHERE topic_id = ?", (topic_id,))
    sources = [dict(r) for r in cur.fetchall()]
    conn.close()

    # Categorize claims
    verified_facts = [c["claim_text"] for c in claims if c["is_verified"] == 1]
    speculations = [c["claim_text"] for c in claims if c["is_speculation"] == 1]

    # 3. Dynamic Narrative Construction based on category
    category = topic.get("category", "Facts & Secrets")
    title = topic.get("title", "")
    desc = topic.get("description", "")

    # Hook variations
    hook_templates = {
        "Facts & Secrets": [
            f"Did you notice this insane detail officially confirmed in {game['name']}?",
            f"Here is why everyone is talking about this secret in {game['name']}!",
            f"Rockstar just revealed something massive about {title}!"
        ],
        "Cars & Comparisons": [
            f"How realistic will vehicle physics actually be in {game['name']}?",
            f"This confirmed vehicle feature in {game['name']} changes everything!",
            f"Wait until you see how cars deform in the new {game['name']}!"
        ],
        "Stories": [
            f"The criminal underworld of {game['name']} holds a dark secret...",
            f"What really binds the protagonists of {game['name']} together?",
            f"This official storyline theory about {title} will blow your mind!"
        ]
    }

    hooks = hook_templates.get(category, [f"Here is the truth about {title} in {game['name']}!"])
    selected_hook = random.choice(hooks)

    # Core Body Content
    body_points = []
    if verified_facts:
        for f in verified_facts[:3]:
            body_points.append(f)
    else:
        body_points.append(f"Official developer records confirm that {desc}")

    # Explicit disclosure for speculative claims
    if speculations:
        spec_text = " ".join(speculations[:1])
        body_points.append(f"Keep in mind, community reports suggest {spec_text} — though Rockstar has yet to officially confirm this.")

    closing_lines = [
        f"What feature are you most excited for in {game['name']}? Let us know in the comments!",
        f"Do you think {game['name']} will live up to the hype? Drop your thoughts below!",
        f"Follow for more verified {game['name']} intelligence and breakdowns!"
    ]
    selected_closing = random.choice(closing_lines)

    # 4. Construct Scene Breakdown & Timing
    is_long = (target_duration == "60-90s")
    scenes = []

    if not is_long:
        # 30-50s -> 3 Scenes (Total ~40s)
        # Scene 1: Hook (0 - 8s)
        scenes.append({
            "scene_number": 1,
            "start_time": 0.0,
            "end_time": 8.0,
            "visual_type": "SVG_TYPOGRAPHY",
            "visual_prompt": f"Neon glowing bold title: '{selected_hook}'",
            "narration_text": selected_hook,
            "subtitle_text": selected_hook,
            "transition_type": "fade"
        })
        # Scene 2: Core Facts / Comparison (8 - 30s)
        body_speech = " ".join(body_points)
        scenes.append({
            "scene_number": 2,
            "start_time": 8.0,
            "end_time": 30.0,
            "visual_type": "SVG_MAP" if "Map" in title or "City" in title else "SVG_COMPARISON",
            "visual_prompt": f"Interactive graphic breakdown for: {title}",
            "narration_text": body_speech,
            "subtitle_text": body_speech,
            "transition_type": "slide_left"
        })
        # Scene 3: Conclusion / Call to Action (30 - 40s)
        scenes.append({
            "scene_number": 3,
            "start_time": 30.0,
            "end_time": 40.0,
            "visual_type": "SVG_COUNTDOWN",
            "visual_prompt": "Neon outro card with animated comment prompt",
            "narration_text": selected_closing,
            "subtitle_text": selected_closing,
            "transition_type": "fade"
        })
    else:
        # 60-90s -> 5 Scenes (Total ~70s)
        scenes.append({
            "scene_number": 1,
            "start_time": 0.0,
            "end_time": 10.0,
            "visual_type": "SVG_TYPOGRAPHY",
            "visual_prompt": f"Bold kinetic intro hook: '{selected_hook}'",
            "narration_text": selected_hook,
            "subtitle_text": selected_hook,
            "transition_type": "fade"
        })
        scenes.append({
            "scene_number": 2,
            "start_time": 10.0,
            "end_time": 25.0,
            "visual_type": "SVG_MAP",
            "visual_prompt": f"Setting & geographical breakdown: {desc[:80]}",
            "narration_text": body_points[0] if len(body_points) > 0 else desc,
            "subtitle_text": body_points[0] if len(body_points) > 0 else desc,
            "transition_type": "wipe"
        })
        scenes.append({
            "scene_number": 3,
            "start_time": 25.0,
            "end_time": 45.0,
            "visual_type": "SVG_COMPARISON",
            "visual_prompt": "Comparative analysis chart & verified visual details",
            "narration_text": body_points[1] if len(body_points) > 1 else "Analysis of official trailer frames reveals massive physics improvements.",
            "subtitle_text": body_points[1] if len(body_points) > 1 else "Analysis of official trailer frames reveals massive physics improvements.",
            "transition_type": "slide_left"
        })
        scenes.append({
            "scene_number": 4,
            "start_time": 45.0,
            "end_time": 60.0,
            "visual_type": "SVG_STORY",
            "visual_prompt": "Character & lore narrative breakdown",
            "narration_text": body_points[2] if len(body_points) > 2 else "Every small environmental choice points to the most ambitious open world ever crafted.",
            "subtitle_text": body_points[2] if len(body_points) > 2 else "Every small environmental choice points to the most ambitious open world ever crafted.",
            "transition_type": "fade"
        })
        scenes.append({
            "scene_number": 5,
            "start_time": 60.0,
            "end_time": 72.0,
            "visual_type": "SVG_COUNTDOWN",
            "visual_prompt": "Outro prompt with verified fact seal",
            "narration_text": selected_closing,
            "subtitle_text": selected_closing,
            "transition_type": "fade"
        })

    # 5. Full Voiceover Text
    full_voiceover = " ".join([s["narration_text"] for s in scenes])

    # 6. Publishing Metadata
    game_clean = game['name'].replace(" ", "")
    hashtags = f"#{game_clean} #GTA6 #GTA #{category.replace(' ', '').replace('&', '')} #Gaming #Shorts #TikTokGaming"
    yt_title = f"{title[:50]} | {game['name']} #Shorts"
    
    source_citation_str = ""
    if sources:
        source_citation_str = f"\n\nVerified Sources:\n- " + "\n- ".join([f"{s['source_name']}: {s['url']}" for s in sources[:2]])

    yt_desc = (
        f"{desc}\n\n"
        f"Educational gaming breakdown and verified intelligence for {game['name']}.\n"
        f"All commentary and vector visualizations are original transformations.{source_citation_str}\n\n"
        f"{hashtags}"
    )

    tiktok_caption = f"{selected_hook[:70]}... {hashtags}"

    # 7. Record Script into SQLite
    script_id = f"scr-{int(datetime.now().timestamp())}-{random.randint(100, 999)}"
    now = datetime.now().isoformat()

    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO scripts (
            id, topic_id, game_id, title, category, target_duration, hook, body, closing,
            voiceover_text, full_script, scene_count, hashtags, youtube_title,
            youtube_description, tiktok_caption, status, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'GENERATED', ?)
        """, (
            script_id, topic_id, actual_game_id, title, category, target_duration,
            selected_hook, " ".join(body_points), selected_closing, full_voiceover,
            json.dumps(scenes), len(scenes), hashtags, yt_title, yt_desc, tiktok_caption, now
        ))

        # Also register default video_project linked to this script
        project_id = f"proj-{script_id[4:]}"
        cur.execute("""
        INSERT INTO video_projects (
            id, script_id, game_id, project_name, status, target_resolution,
            aspect_ratio, fps, quality_preset, duration_seconds, created_at, updated_at
        ) VALUES (?, ?, ?, ?, 'PENDING', '1080x1920', '9:16', 30, 'ultrafast', ?, ?, ?)
        """, (
            project_id, script_id, actual_game_id, f"{game['name']} - {title[:30]}",
            scenes[-1]["end_time"], now, now
        ))

        # Record individual scenes
        for sc in scenes:
            cur.execute("""
            INSERT INTO video_scenes (
                id, project_id, scene_number, start_time, end_time, visual_type,
                visual_prompt, narration_text, subtitle_text, transition_type, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                f"scn-{project_id[5:]}-{sc['scene_number']}",
                project_id, sc["scene_number"], sc["start_time"], sc["end_time"],
                sc["visual_type"], sc["visual_prompt"], sc["narration_text"],
                sc["subtitle_text"], sc["transition_type"], now
            ))

        conn.commit()
    finally:
        conn.close()

    return {
        "success": True,
        "script_id": script_id,
        "project_id": project_id,
        "title": title,
        "duration": target_duration,
        "scene_count": len(scenes),
        "scenes": scenes,
        "hook": selected_hook,
        "voiceover_text": full_voiceover,
        "youtube_title": yt_title,
        "youtube_description": yt_desc,
        "tiktok_caption": tiktok_caption,
        "hashtags": hashtags
    }

if __name__ == "__main__":
    import pprint
    # Test on seed topic
    res = generate_script_for_topic("top-gta6-001", "30-50s")
    pprint.pprint(res)
