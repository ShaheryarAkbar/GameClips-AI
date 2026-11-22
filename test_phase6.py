"""
GameClips AI - Phase 6 Test Suite: Export Center, Analytics & Automation Scheduling
Tests:
- Export Center: Strict human approval gate, self-contained release package, all metadata TXT files, separated YouTube/TikTok subfolders, copyright report.
- Analytics Engine: Funnel aggregation, category breakdown, compliance index, disk headroom monitoring.
- Automation Scheduler: Daily candidate quota, storage headroom gate, queueing to Approval Queue, zero auto-publishing.
- Flask API Endpoints for exports, analytics, and automation.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database, get_connection
from script_generator import generate_script_for_topic
from video_engine import render_video_project
from verification_engine import verify_project_compliance, record_approval_decision
from export_manager import export_approved_project, list_all_exports, get_export_by_id
from analytics_engine import get_analytics_summary
from scheduler import get_scheduler_status, run_automation_cycle
from app import app

class TestPhase6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.client = app.test_client()

        # Prepare a project for export testing
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' AND is_duplicate = 0 LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        script_res = generate_script_for_topic(topic_id, target_duration="30-50s")
        cls.project_id = script_res["project_id"]
        cls.render_res = render_video_project(cls.project_id, is_preview=True, quality_preset="ultrafast")
        verify_project_compliance(cls.project_id)

    def test_01_export_unapproved_project_blocked(self):
        """Verify export is strictly BLOCKED if the project is not APPROVED by a human."""
        # Project is currently PENDING/NEEDS_REVIEW
        res = export_approved_project(self.project_id)
        self.assertFalse(res["success"])
        self.assertIn("must be APPROVED", res["error"])

    def test_02_export_approved_project_package(self):
        """Verify complete package generation when project is APPROVED."""
        # 1. Human Approves the Project
        appr_res = record_approval_decision(
            project_id=self.project_id,
            action="APPROVE",
            reviewer_notes="Phase 6 test approval.",
            warning_acknowledged=True
        )
        self.assertTrue(appr_res["success"])

        # 2. Trigger Export
        res = export_approved_project(self.project_id)
        self.assertTrue(res["success"], msg=res.get("error"))
        self.assertIn("export_id", res)
        self.cls_export_id = res["export_id"]

        package_dir = res["package_folder"]
        self.assertTrue(os.path.exists(package_dir))

        # 3. Check Required Files
        expected_files = [
            "final_video.mp4",
            "thumbnail.png",
            "Title.txt",
            "Description.txt",
            "Hashtags.txt",
            "Sources.txt",
            "Copyright_Report.txt",
            os.path.join("youtube_package", "yt_title.txt"),
            os.path.join("youtube_package", "yt_description.txt"),
            os.path.join("youtube_package", "yt_tags.txt"),
            os.path.join("tiktok_package", "tiktok_caption.txt"),
            os.path.join("tiktok_package", "tiktok_tags.txt")
        ]
        for f in expected_files:
            file_path = os.path.join(package_dir, f)
            self.assertTrue(os.path.exists(file_path), f"Missing expected export file: {f}")
            self.assertGreater(os.path.getsize(file_path), 0, f"File {f} is empty")

        # 4. Check Copyright Report contains mandatory disclaimer and anti-misrepresentation
        with open(os.path.join(package_dir, "Copyright_Report.txt"), "r", encoding="utf-8") as cr:
            report_text = cr.read()
            self.assertIn("Automated detection and verification checks do NOT guarantee 100% legal immunity", report_text)
            self.assertIn("Human Approval Status:   APPROVED", report_text)
            self.assertIn("Windows SAPI", report_text)

        # 5. Check SQLite registration in exported_videos
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM exported_videos WHERE project_id = ?", (self.project_id,))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["video_path"], os.path.join(package_dir, "final_video.mp4"))

    def test_03_analytics_engine_aggregation(self):
        """Verify analytics engine computes funnel, safety score, and storage metrics."""
        summary = get_analytics_summary()
        self.assertIn("funnel", summary)
        self.assertIn("topics", summary)
        self.assertIn("compliance_safety", summary)
        self.assertIn("storage", summary)

        funnel = summary["funnel"]
        self.assertGreater(funnel["topics_discovered"], 0)
        self.assertGreater(funnel["scripts_generated"], 0)
        self.assertGreater(funnel["videos_rendered"], 0)
        self.assertGreater(funnel["approved"], 0)
        self.assertGreater(funnel["exported"], 0)
        self.assertGreater(funnel["approval_rate_percent"], 0)

        safety = summary["compliance_safety"]
        self.assertTrue(safety["disclaimer_enforced"])
        self.assertGreaterEqual(safety["safety_score_index"], 0.0)

        storage = summary["storage"]
        self.assertTrue(storage["is_safe_to_render"])
        self.assertIn("project_drive", storage)

    def test_04_automation_scheduler_cycle(self):
        """Verify scheduler status checks and candidate production into Approval Queue."""
        status = get_scheduler_status()
        self.assertIn("daily_video_target", status)
        self.assertEqual(status["auto_publishing_allowed"], False) # Strict rule!
        self.assertTrue(status["is_safe_to_render"])

        # Run 1 candidate cycle
        res = run_automation_cycle(game_id="game-gta6", max_candidates=1, force_preview=True)
        self.assertTrue(res["success"], msg=res.get("error"))
        self.assertGreaterEqual(res["candidates_generated"], 1)

        candidate = res["queued_projects"][0]
        self.assertEqual(candidate["status"], "NEEDS_REVIEW")
        self.assertTrue(os.path.exists(candidate["video_path"]))

        # Check DB project status is NEEDS_REVIEW (strictly in Approval Queue)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT status FROM video_projects WHERE id = ?", (candidate["project_id"],))
        p_status = cur.fetchone()[0]
        conn.close()
        self.assertEqual(p_status, "NEEDS_REVIEW")

    def test_05_api_export_and_analytics_endpoints(self):
        """Verify Flask API endpoints for export listing, details, file streaming, and analytics."""
        # 1. GET /api/exports
        res_exp = self.client.get("/api/exports")
        self.assertEqual(res_exp.status_code, 200)
        exp_list = res_exp.get_json()
        self.assertIsInstance(exp_list, list)
        self.assertGreater(len(exp_list), 0)

        first_exp = exp_list[0]
        export_id = first_exp["id"]

        # 2. GET /api/exports/<id>
        res_single = self.client.get(f"/api/exports/{export_id}")
        self.assertEqual(res_single.status_code, 200)
        self.assertEqual(res_single.get_json()["id"], export_id)

        # 3. GET /api/exports/<id>/file/Title.txt
        res_file = self.client.get(f"/api/exports/{export_id}/file/Title.txt")
        self.assertEqual(res_file.status_code, 200)
        self.assertGreater(len(res_file.data), 0)

        # 4. GET /api/analytics
        res_ana = self.client.get("/api/analytics")
        self.assertEqual(res_ana.status_code, 200)
        ana_data = res_ana.get_json()
        self.assertIn("funnel", ana_data)

        # 5. GET /api/automation/status
        res_auto = self.client.get("/api/automation/status")
        self.assertEqual(res_auto.status_code, 200)
        self.assertEqual(res_auto.get_json()["auto_publishing_allowed"], False)

if __name__ == "__main__":
    unittest.main()
