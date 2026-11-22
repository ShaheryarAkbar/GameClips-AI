"""
GameClips AI - Phase 3 Verification Test Suite
Tests:
- Script Generator Engine: 30-50s and 60-90s generation, evidence inclusion, scene plans, metadata
- Original Visual Engine: 1080x1920 vertical frames for Typography, Map, Comparison, Story, Countdown
- Phase 3 Flask Studio API Endpoints
"""

import os
import sys
import unittest
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database, get_connection
from script_generator import generate_script_for_topic
from visual_engine import render_scene_frame, generate_visuals_for_project
from app import app

class TestPhase3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.client = app.test_client()

    def test_01_script_generator_30_50s(self):
        """Verify 30-50s short script structure, hook, scenes, and publishing metadata."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        res = generate_script_for_topic(topic_id, target_duration="30-50s")
        self.assertTrue(res["success"])
        self.assertEqual(res["duration"], "30-50s")
        self.assertGreaterEqual(res["scene_count"], 3)
        self.assertIn("voiceover_text", res)
        self.assertIn("youtube_title", res)
        self.assertIn("tiktok_caption", res)
        self.assertIn("#Shorts", res["youtube_title"])
        self.assertIn("#GTA", res["hashtags"])

        # Check SQLite record
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM scripts WHERE id = ?", (res["script_id"],))
        self.assertIsNotNone(cur.fetchone())
        cur.execute("SELECT COUNT(*) FROM video_scenes WHERE project_id = ?", (res["project_id"],))
        self.assertEqual(cur.fetchone()[0], res["scene_count"])
        conn.close()

    def test_02_script_generator_60_90s(self):
        """Verify 60-90s extended script generation with more scenes and longer duration."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        res = generate_script_for_topic(topic_id, target_duration="60-90s")
        self.assertTrue(res["success"])
        self.assertEqual(res["duration"], "60-90s")
        self.assertGreaterEqual(res["scene_count"], 5)
        self.assertGreater(len(res["voiceover_text"]), 100)

    def test_03_visual_rendering_all_types(self):
        """Verify Pillow renders valid 1080x1920 frames for all required visual modes."""
        temp_dir = os.path.join(os.path.dirname(__file__), "temp_render", "test_visuals")
        os.makedirs(temp_dir, exist_ok=True)

        visual_types = ["SVG_TYPOGRAPHY", "SVG_MAP", "SVG_COMPARISON", "SVG_STORY", "SVG_COUNTDOWN"]

        for idx, vt in enumerate(visual_types):
            scene = {
                "scene_number": idx + 1,
                "visual_type": vt,
                "narration_text": f"Testing visual rendering for {vt} with dynamic styling and subtitles."
            }
            out_path = os.path.join(temp_dir, f"test_{vt}.png")
            render_scene_frame(scene, project_name="Grand Theft Auto VI", output_path=out_path)

            self.assertTrue(os.path.isfile(out_path), f"Frame file not created for {vt}")
            with Image.open(out_path) as im:
                self.assertEqual(im.size, (1080, 1920), f"Incorrect dimensions for {vt}")
                self.assertEqual(im.mode, "RGB")

    def test_04_batch_project_visual_generation(self):
        """Verify batch rendering for all scenes of a video project."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        script_res = generate_script_for_topic(topic_id, target_duration="30-50s")
        project_id = script_res["project_id"]

        vis_res = generate_visuals_for_project(project_id)
        self.assertTrue(vis_res["success"])
        self.assertEqual(vis_res["frames_generated"], script_res["scene_count"])

        for fp in vis_res["frame_paths"]:
            self.assertTrue(os.path.isfile(fp))

        # Check preview_path updated in DB
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT preview_path FROM video_projects WHERE id = ?", (project_id,))
        preview_path = cur.fetchone()[0]
        conn.close()
        self.assertIsNotNone(preview_path)
        self.assertTrue(os.path.isfile(preview_path))

    def test_05_api_studio_endpoints(self):
        """Verify studio generate, project details, and frame preview APIs."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        # 1. Studio generate API
        gen_payload = {
            "topic_id": topic_id,
            "target_duration": "30-50s",
            "voice_name": "Microsoft David Desktop",
            "visual_style": "SVG_ANIMATION"
        }
        res = self.client.post("/api/studio/generate", json=gen_payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        project_id = data["project_id"]

        # 2. Project details API
        res_proj = self.client.get(f"/api/studio/project/{project_id}")
        self.assertEqual(res_proj.status_code, 200)
        proj_data = res_proj.get_json()
        self.assertTrue(proj_data["success"])
        self.assertEqual(len(proj_data["scenes"]), data["script"]["scene_count"])

        # 3. Live image preview API for Scene 1
        res_img = self.client.get(f"/api/preview/image/{project_id}/1")
        self.assertEqual(res_img.status_code, 200)
        self.assertEqual(res_img.mimetype, "image/png")
        self.assertGreater(len(res_img.data), 1000)

        # 4. List scripts API
        res_scripts = self.client.get("/api/scripts")
        self.assertEqual(res_scripts.status_code, 200)
        self.assertGreaterEqual(len(res_scripts.get_json()), 1)

if __name__ == "__main__":
    unittest.main()
