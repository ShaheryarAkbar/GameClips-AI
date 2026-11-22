"""
GameClips AI - Phase 1 Verification Test Suite
Tests:
- Database schema and integrity
- Multi-game modular configuration
- Storage management and threshold safety
- Flask API routes & template rendering
- FFmpeg availability
"""

import os
import sys
import json
import unittest
import subprocess

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database, get_connection
from storage_manager import get_disk_status, cleanup_temporary_files
from app import app

class TestPhase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.client = app.test_client()

    def test_01_database_tables(self):
        """Verify all 14 required SQLite tables exist."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cur.fetchall()]
        conn.close()

        required_tables = [
            "games", "topics", "research_sources", "factual_claims",
            "scripts", "video_projects", "video_scenes", "footage_assets",
            "asset_licenses", "audio_assets", "verification_reports",
            "approval_history", "exported_videos", "system_settings"
        ]
        for t in required_tables:
            self.assertIn(t, tables, f"Missing required table: {t}")

    def test_02_seeded_games(self):
        """Verify multi-game library seeds correctly with GTA 6 active."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT slug, is_active FROM games")
        games = dict(cur.fetchall())
        conn.close()

        expected_slugs = ["gta-6", "gta-5", "gta-4", "gta-san-andreas", "gta-vice-city", "gta-3", "rdr-2", "minecraft"]
        for slug in expected_slugs:
            self.assertIn(slug, games, f"Missing game: {slug}")

        self.assertEqual(games["gta-6"], 1, "GTA 6 must be the default active game")

    def test_03_storage_manager(self):
        """Verify disk space metrics and headroom checks."""
        status = get_disk_status()
        self.assertIn("project_drive", status)
        self.assertIn("os_drive", status)
        self.assertIn("thresholds", status)
        self.assertGreater(status["project_drive"]["free_gb"], 0)
        self.assertTrue(status["is_safe_to_render"])

    def test_04_api_health(self):
        """Verify health check endpoint."""
        res = self.client.get("/api/health")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "healthy")

    def test_05_api_stats(self):
        """Verify dashboard statistics endpoint."""
        res = self.client.get("/api/stats")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("active_game", data)
        self.assertEqual(data["active_game"]["slug"], "gta-6")
        self.assertGreaterEqual(data["topics_count"], 3)

    def test_06_api_games_and_activation(self):
        """Verify listing games, switching active game, and adding a new game."""
        # List games
        res = self.client.get("/api/games")
        self.assertEqual(res.status_code, 200)
        games = res.get_json()
        self.assertGreaterEqual(len(games), 8)

        # Switch to Minecraft
        res = self.client.post("/api/games/game-minecraft/activate")
        self.assertEqual(res.status_code, 200)

        # Confirm Minecraft is active
        res = self.client.get("/api/stats")
        self.assertEqual(res.get_json()["active_game"]["slug"], "minecraft")

        # Switch back to GTA 6
        self.client.post("/api/games/game-gta6/activate")

        # Test Add New Game
        new_game = {
            "name": "Elden Ring",
            "developer": "FromSoftware",
            "publisher": "Bandai Namco",
            "official_sources": "https://www.bandainamcoent.com",
            "fan_content_policy_url": "https://www.fromsoftware.jp/en/guidelines.html",
            "commercial_rules": "Gameplay videos allowed with commentary. No music monetization."
        }
        res = self.client.post("/api/games/add", json=new_game)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.get_json()["success"])

    def test_07_api_settings_update(self):
        """Verify updating system settings."""
        res = self.client.post("/api/settings", json={"render_preset": "ultrafast", "storage_limit_gb": "2.5"})
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.get_json()["success"])

        # Check updated setting
        res = self.client.get("/api/settings")
        data = res.get_json()
        self.assertEqual(data["settings"]["render_preset"], "ultrafast")
        self.assertEqual(data["settings"]["storage_limit_gb"], "2.5")

    def test_08_index_page(self):
        """Verify dashboard HTML rendering."""
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)
        self.assertIn("GameClips", html)
        self.assertIn("Command Center", html)
        self.assertIn("Approval Queue", html)

    def test_09_ffmpeg_presence(self):
        """Verify FFmpeg is accessible via subprocess."""
        result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("ffmpeg version", result.stdout)

if __name__ == "__main__":
    unittest.main()
