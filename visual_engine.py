"""
GameClips AI - Original Visual Generation Engine
Produces high-resolution 1080x1920 (9:16 vertical) vector & graphic frames
for YouTube Shorts and TikTok without requiring GPU or heavy AI models.
"""

import os
import math
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from database import get_connection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp_render")

# Color palette (Cyberpunk / Leonida Neon Gaming Theme)
COLOR_BG_DARK = (11, 14, 20)        # #0B0E14
COLOR_CARD_BG = (22, 27, 38)        # #161B26
COLOR_CYAN = (0, 240, 255)          # #00F0FF
COLOR_PINK = (255, 42, 133)         # #FF2A85
COLOR_LIME = (0, 255, 136)          # #00FF88
COLOR_GOLD = (255, 184, 0)          # #FFB800
COLOR_TEXT_WHITE = (240, 244, 252)  # #F0F4FC
COLOR_TEXT_MUTED = (140, 150, 170)  # #8C96AA
COLOR_BORDER = (40, 50, 70)

def get_font(size=36, bold=False):
    """Retrieves standard Windows TrueType font or falls back gracefully."""
    font_paths = [
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\calibri.ttf"
    ]
    if bold:
        font_paths = [
            "C:\\Windows\\Fonts\\segoeuib.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf"
        ] + font_paths

    for fp in font_paths:
        if os.path.isfile(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()

def wrap_text(text, font, max_width, draw):
    """Wraps text so it fits comfortably within the specified canvas width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def create_base_canvas(width=1080, height=1920):
    """Creates a sleek 9:16 vertical canvas with subtle cyber grid accents."""
    img = Image.new("RGB", (width, height), COLOR_BG_DARK)
    draw = ImageDraw.Draw(img)

    # 1. Subtle horizontal and vertical tech grid lines
    grid_color = (20, 26, 38)
    for y in range(0, height, 80):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
    for x in range(0, width, 80):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)

    # 2. Top Header Branding Banner
    draw.rectangle([60, 60, width - 60, 140], fill=COLOR_CARD_BG, outline=COLOR_BORDER, width=2)
    font_brand = get_font(32, bold=True)
    draw.text((90, 82), "GameClips", font=font_brand, fill=COLOR_TEXT_WHITE)
    bbox_gc = draw.textbbox((90, 82), "GameClips", font=font_brand)
    draw.text((bbox_gc[2] + 4, 82), "AI", font=font_brand, fill=COLOR_CYAN)

    font_badge = get_font(20, bold=True)
    draw.rectangle([width - 320, 78, width - 90, 122], fill=(0, 240, 255, 30), outline=COLOR_CYAN, width=1)
    draw.text((width - 305, 88), "VERIFIED INTEL", font=font_badge, fill=COLOR_CYAN)

    # 3. Outer glowing border
    draw.rectangle([40, 40, width - 40, height - 40], outline=COLOR_BORDER, width=2)

    return img, draw

def render_scene_frame(scene, project_name="GTA 6", output_path=None):
    """
    Renders an original, high-impact 1080x1920 frame for a scene:
    Supports SVG_TYPOGRAPHY, SVG_MAP, SVG_COMPARISON, SVG_STORY, SVG_COUNTDOWN.
    """
    width, height = 1080, 1920
    img, draw = create_base_canvas(width, height)
    v_type = scene.get("visual_type", "SVG_TYPOGRAPHY")
    narration = scene.get("narration_text", "")
    scene_num = scene.get("scene_number", 1)

    font_title = get_font(52, bold=True)
    font_sub = get_font(38)
    font_label = get_font(26, bold=True)

    # Center card area: (80, 200) to (1000, 1500)
    card_x0, card_y0 = 80, 200
    card_x1, card_y1 = 1000, 1520
    draw.rectangle([card_x0, card_y0, card_x1, card_y1], fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=3)

    # Scene step badge inside card
    draw.rectangle([card_x0 + 40, card_y0 + 40, card_x0 + 260, card_y0 + 90], fill=COLOR_BG_DARK, outline=COLOR_PINK, width=2)
    draw.text((card_x0 + 55, card_y0 + 50), f"PHASE // 0{scene_num}", font=font_label, fill=COLOR_PINK)

    # Scene Type specific visual rendering
    if v_type == "SVG_MAP":
        # Draw tech radar & map geometry
        center_x, center_y = 540, 680
        radius = 260
        # Radar circles
        for r in [60, 130, 200, radius]:
            draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], outline=COLOR_CYAN, width=2)
        draw.line([center_x - radius, center_y, center_x + radius, center_y], fill=COLOR_CYAN, width=1)
        draw.line([center_x, center_y - radius, center_x, center_y + radius], fill=COLOR_CYAN, width=1)
        # Radar sweep vector
        draw.line([center_x, center_y, center_x + 180, center_y - 180], fill=COLOR_LIME, width=4)
        # Waypoint marker
        draw.polygon([(center_x + 80, center_y - 90), (center_x + 65, center_y - 60), (center_x + 95, center_y - 60)], fill=COLOR_PINK)
        draw.text((center_x - 140, center_y + radius + 30), "LEONIDA STATE // VICE CITY", font=font_label, fill=COLOR_CYAN)

    elif v_type == "SVG_COMPARISON":
        # Side-by-side comparison bars
        bar_y_start = 500
        # Item A: Los Santos (GTA 5)
        draw.text((card_x0 + 60, bar_y_start), "GTA V (Los Santos)", font=font_label, fill=COLOR_TEXT_MUTED)
        draw.rectangle([card_x0 + 60, bar_y_start + 40, card_x0 + 380, bar_y_start + 90], fill=(50, 60, 80), outline=COLOR_BORDER)
        draw.text((card_x0 + 400, bar_y_start + 50), "75 km²", font=font_label, fill=COLOR_TEXT_WHITE)

        # Item B: Leonida (GTA 6)
        bar_y_b = bar_y_start + 140
        draw.text((card_x0 + 60, bar_y_b), "GTA VI (State of Leonida)", font=font_label, fill=COLOR_CYAN)
        draw.rectangle([card_x0 + 60, bar_y_b + 40, card_x0 + 760, bar_y_b + 90], fill=COLOR_CYAN, outline=COLOR_LIME)
        draw.text((card_x0 + 780, bar_y_b + 50), "190+ km²", font=font_label, fill=COLOR_LIME)

        # Scale indicator
        draw.text((card_x0 + 60, bar_y_b + 130), "SCALE INCREASE: ~2.5x EXPANSION", font=font_label, fill=COLOR_GOLD)

    elif v_type == "SVG_STORY":
        # Dramatic story & dialogue silhouette layout
        draw.rectangle([card_x0 + 50, 480, card_x1 - 50, 880], fill=COLOR_BG_DARK, outline=COLOR_PINK, width=2)
        font_quote = get_font(72, bold=True)
        draw.text((card_x0 + 80, 490), "“", font=font_quote, fill=COLOR_PINK)
        story_lines = wrap_text(narration[:120], font_sub, 780, draw)
        sy = 580
        for sl in story_lines[:4]:
            draw.text((card_x0 + 100, sy), sl, font=font_sub, fill=COLOR_TEXT_WHITE)
            sy += 50
        draw.text((card_x1 - 320, 820), "— LUCIA & JASON", font=font_label, fill=COLOR_CYAN)

    elif v_type == "SVG_COUNTDOWN":
        # Outro / Call to action layout
        draw.ellipse([440, 520, 640, 720], fill=COLOR_BG_DARK, outline=COLOR_GOLD, width=4)
        draw.text((505, 580), "★", font=get_font(80), fill=COLOR_GOLD)
        draw.text((360, 760), "COMMUNITY VOTE", font=font_label, fill=COLOR_GOLD)

    else:
        # Default: SVG_TYPOGRAPHY (High-impact kinetic hook)
        draw.rectangle([card_x0 + 60, 480, card_x1 - 60, 500], fill=COLOR_CYAN)
        hook_lines = wrap_text(narration[:140], font_title, 800, draw)
        hy = 560
        for hl in hook_lines[:4]:
            draw.text((card_x0 + 60, hy), hl, font=font_title, fill=COLOR_TEXT_WHITE)
            hy += 70

    # Narration / Subtitle Lower-Third Area (1560 to 1840)
    sub_bg = (16, 20, 29)
    draw.rectangle([60, 1560, width - 60, 1840], fill=sub_bg, outline=COLOR_CYAN, width=2)
    draw.text((90, 1580), "SUBTITLES // AUDIO SYNC", font=get_font(20, bold=True), fill=COLOR_PINK)

    sub_lines = wrap_text(narration, font_sub, width - 200, draw)
    text_y = 1625
    for line in sub_lines[:3]:
        draw.text((90, text_y), line, font=font_sub, fill=COLOR_TEXT_WHITE)
        text_y += 50

    # Save output frame
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, "PNG")

    return img

def generate_visuals_for_project(project_id):
    """
    Renders 1080x1920 frames for every scene in a video project
    and records their local file paths in the database.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()

        cur.execute("SELECT * FROM video_projects WHERE id = ?", (project_id,))
        p_row = cur.fetchone()
        if not p_row:
            return {"success": False, "error": "Project not found."}

        project = dict(p_row)

        cur.execute("SELECT * FROM video_scenes WHERE project_id = ? ORDER BY scene_number ASC", (project_id,))
        scenes = [dict(r) for r in cur.fetchall()]

        if not scenes:
            return {"success": False, "error": "No scenes found for project."}

        visual_dir = os.path.join(TEMP_DIR, "visuals", project_id)
        os.makedirs(visual_dir, exist_ok=True)

        generated_frames = []
        for sc in scenes:
            out_file = os.path.join(visual_dir, f"scene_{sc['scene_number']}.png")
            render_scene_frame(sc, project_name=project.get("project_name", "Gaming"), output_path=out_file)

            # Update DB scene record
            cur.execute("UPDATE video_scenes SET visual_asset_path = ? WHERE id = ?", (out_file, sc["id"]))
            generated_frames.append(out_file)

        # Set project preview path to the first generated frame
        if generated_frames:
            cur.execute("UPDATE video_projects SET preview_path = ?, updated_at = ? WHERE id = ?", (
                generated_frames[0], datetime.now().isoformat(), project_id
            ))

        conn.commit()

        return {
            "success": True,
            "project_id": project_id,
            "frames_generated": len(generated_frames),
            "frame_paths": generated_frames
        }
    finally:
        conn.close()

if __name__ == "__main__":
    # Quick self-test
    test_scene = {
        "scene_number": 1,
        "visual_type": "SVG_MAP",
        "narration_text": "Rockstar officially confirmed GTA 6 takes place in the state of Leonida, encompassing Vice City!"
    }
    test_out = os.path.join(TEMP_DIR, "test_render_frame.png")
    render_scene_frame(test_scene, "GTA 6", test_out)
    print(f"[OK] Rendered test frame to: {test_out}")
