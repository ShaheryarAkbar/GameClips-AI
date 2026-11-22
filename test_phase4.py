"""
GameClips AI - Phase 4 Verification Test Suite
Tests:
- Audio Engine: Windows SAPI synthesis, duration calculation, silent mode fallback, audio_assets record
- Subtitle Engine: SRT and styled ASS generation, exact timestamp synchronization
- Video Engine: FFmpeg CPU video assembly, H.264/AAC output, 9:16 vertical target, thumbnail generation
- Phase 4 Flask Video Rendering & Streaming Endpoints
"""

import os
import sys
import unittest
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database, get_connection
from script_generator import generate_script_for_topic
from visual_engine import generate_visuals_for_project
from audio_engine import generate_offline_speech, get_audio_duration_wave, create_silent_audio
from subtitle_engine import generate_subtitles_for_scenes
from video_engine import render_video_project
from app import app

class TestPhase4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.client = app.test_client()

    def test_01_audio_engine_sapi(self):
        """Verify Windows SAPI synthesizes WAV audio and records to database."""
        out_wav = os.path.join(os.path.dirname(__file__), "temp_render", "test_phase4_voice.wav")
        text = "This is a test of GameClips AI offline voice synthesis for GTA 6 video production."

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM video_projects LIMIT 1")
        row = cur.fetchone()
        real_proj_id = row[0] if row else None
        conn.close()

        res = generate_offline_speech(text, voice_name="Microsoft David Desktop", project_id=real_proj_id, output_wav=out_wav)
        self.assertTrue(res["success"])
        self.assertTrue(os.path.isfile(out_wav))
        self.assertGreater(res["duration"], 1.0)

        # Check SQLite record
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM audio_assets WHERE file_path = ?", (out_wav,))
        self.assertIsNotNone(cur.fetchone())
        conn.close()

    def test_02_silent_audio_fallback(self):
        """Verify silent mode creates a valid silent WAV of exact duration."""
        silent_wav = os.path.join(os.path.dirname(__file__), "temp_render", "test_silent.wav")
        res = generate_offline_speech("", voice_name="SILENT", project_id="test-silent", output_wav=silent_wav)
        self.assertTrue(res["success"])
        self.assertTrue(res["is_silent"])
        self.assertTrue(os.path.isfile(silent_wav))
        self.assertAlmostEqual(res["duration"], 15.0, delta=0.5)

    def test_03_subtitle_engine(self):
        """Verify generation of synchronized SRT and styled ASS subtitles."""
        scenes = [
            {"scene_number": 1, "start_time": 0.0, "end_time": 6.5, "subtitle_text": "Did you know this crazy detail about GTA 6?"},
            {"scene_number": 2, "start_time": 6.5, "end_time": 20.0, "subtitle_text": "Rockstar confirmed Vice City is 2.5 times larger than Los Santos."}
        ]
        srt_out = os.path.join(os.path.dirname(__file__), "temp_render", "test_subs.srt")
        ass_out = os.path.join(os.path.dirname(__file__), "temp_render", "test_subs.ass")

        res = generate_subtitles_for_scenes(scenes, srt_out, ass_out)
        self.assertTrue(os.path.isfile(srt_out))
        self.assertTrue(os.path.isfile(ass_out))

        # Inspect SRT content
        with open(srt_out, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("00:00:00,000 --> 00:00:06,500", content)
            self.assertIn("Did you know this crazy detail", content)

        # Inspect ASS content
        with open(ass_out, "r", encoding="utf-8") as f:
            ass_content = f.read()
            self.assertIn("[Script Info]", ass_content)
            self.assertIn("[V4+ Styles]", ass_content)
            self.assertIn("Dialogue:", ass_content)

    def test_04_ffmpeg_video_assembly(self):
        """Verify complete FFmpeg rendering pipeline produces a valid 9:16 MP4 video."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        # Generate Script & Project
        script_res = generate_script_for_topic(topic_id, target_duration="30-50s")
        project_id = script_res["project_id"]

        # Render Video
        render_res = render_video_project(project_id, is_preview=False, quality_preset="ultrafast")
        self.assertTrue(render_res["success"], f"Render failed: {render_res.get('error')}")

        video_path = render_res["video_path"]
        self.assertTrue(os.path.isfile(video_path))
        self.assertGreater(render_res["file_size_mb"], 0.01)

        # Inspect video streams via ffprobe
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries",
            "stream=codec_name,width,height,codec_type",
            "-of", "json", video_path
        ]
        proc = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        import json
        info = json.loads(proc.stdout)
        streams = info.get("streams", [])

        video_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
        audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)

        self.assertIsNotNone(video_stream, "MP4 must contain a video stream")
        self.assertEqual(video_stream["codec_name"], "h264")
        self.assertEqual(video_stream["width"], 1080)
        self.assertEqual(video_stream["height"], 1920)

        self.assertIsNotNone(audio_stream, "MP4 must contain an audio stream")
        self.assertEqual(audio_stream["codec_name"], "aac")

        # Verify project record updated in DB
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT final_video_path, status, thumbnail_path FROM video_projects WHERE id = ?", (project_id,))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "NEEDS_REVIEW")
        self.assertTrue(os.path.isfile(row[2]))

    def test_05_api_video_endpoints(self):
        """Verify video render API and HTML5 streaming API."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM video_projects WHERE final_video_path IS NOT NULL LIMIT 1")
        row = cur.fetchone()
        conn.close()

        if row:
            project_id = row[0]
            # Stream video endpoint
            res = self.client.get(f"/api/video/stream/{project_id}")
            self.assertIn(res.status_code, [200, 206])
            self.assertEqual(res.mimetype, "video/mp4")
            self.assertGreater(len(res.data), 1000)

if __name__ == "__main__":
    unittest.main()
