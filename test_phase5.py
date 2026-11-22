"""
GameClips AI - Phase 5 Verification Test Suite
Tests:
- Verification Engine: 8-point copyright and quality checks, anti-misrepresentation, disclaimer
- Approval System: human sign-off actions (APPROVE, REJECT, REGENERATE), approval_history audit logs
- Metadata editor: updating titles, descriptions, and hashtags before sign-off
- Phase 5 Flask Approval & Verification Endpoints
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database, get_connection
from script_generator import generate_script_for_topic
from video_engine import render_video_project
from verification_engine import verify_project_compliance, record_approval_decision, DISCLAIMER_NOTICE
from app import app

class TestPhase5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.client = app.test_client()

        # Prepare a rendered project for verification testing
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        script_res = generate_script_for_topic(topic_id, target_duration="30-50s")
        cls.project_id = script_res["project_id"]
        cls.render_res = render_video_project(cls.project_id, is_preview=True, quality_preset="ultrafast")

    def test_01_verification_compliance_check(self):
        """Verify 8-point automated compliance check returns VERIFIED status and disclaimer."""
        report = verify_project_compliance(self.project_id)
        self.assertTrue(report["success"])
        self.assertIn(report["status"], ["VERIFIED", "NEEDS_REVIEW"])
        self.assertIn("quality", report)
        self.assertTrue(report["quality"]["passed"])
        self.assertTrue(report["quality"]["is_vertical_9_16"])
        self.assertIn("Automated detection does not guarantee 100% legal immunity", report["disclaimer"])

        # Check SQLite record in verification_reports
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM verification_reports WHERE project_id = ?", (self.project_id,))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["copyright_risk_level"], report["risk_level"])

    def test_02_approval_decision_approve(self):
        """Verify human approval transitions status to APPROVED and records audit log."""
        res = record_approval_decision(
            project_id=self.project_id,
            action="APPROVE",
            reviewer_notes="Verified original vectors and verified citations. Approved.",
            warning_acknowledged=True
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["new_status"], "APPROVED")

        # Verify DB project status and approval_history entry
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT status FROM video_projects WHERE id = ?", (self.project_id,))
        self.assertEqual(cur.fetchone()[0], "APPROVED")

        cur.execute("SELECT * FROM approval_history WHERE project_id = ? AND action = 'APPROVE'", (self.project_id,))
        hist = cur.fetchone()
        self.assertIsNotNone(hist)
        self.assertEqual(hist["rights_warning_acknowledged"], 1)
        conn.close()

    def test_03_approval_decision_reject(self):
        """Verify human rejection transitions status to REJECTED with reviewer notes."""
        res = record_approval_decision(
            project_id=self.project_id,
            action="REJECT",
            reviewer_notes="Audio tone too flat. Rejected for redub.",
            warning_acknowledged=True
        )
        self.assertTrue(res["success"])
        self.assertEqual(res["new_status"], "REJECTED")

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT status FROM video_projects WHERE id = ?", (self.project_id,))
        self.assertEqual(cur.fetchone()[0], "REJECTED")
        conn.close()

    def test_04_approval_decision_regenerate(self):
        """Verify regeneration request resets status to PENDING."""
        res = record_approval_decision(project_id=self.project_id, action="REGENERATE")
        self.assertTrue(res["success"])
        self.assertEqual(res["new_status"], "PENDING")

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT status FROM video_projects WHERE id = ?", (self.project_id,))
        self.assertEqual(cur.fetchone()[0], "PENDING")
        conn.close()

    def test_05_api_approval_endpoints(self):
        """Verify Flask API routes for queue listing, action processing, verify, and metadata editing."""
        # 1. Verification on demand API
        res_v = self.client.post(f"/api/approval/{self.project_id}/verify")
        self.assertEqual(res_v.status_code, 200)
        self.assertTrue(res_v.get_json()["success"])

        # 2. Metadata editing API
        meta_payload = {
            "youtube_title": "GTA 6 Leonida Map Reveal | Mindblowing Scale #Shorts",
            "youtube_description": "Updated description with verified official source citations.",
            "tiktok_caption": "Is GTA 6 really 2.5x bigger than GTA 5? #GTA6",
            "hashtags": "#GTA6 #ViceCity #Gaming"
        }
        res_m = self.client.post(f"/api/approval/{self.project_id}/metadata", json=meta_payload)
        self.assertEqual(res_m.status_code, 200)
        self.assertTrue(res_m.get_json()["success"])

        # 3. Action API: Approve
        res_a = self.client.post(f"/api/approval/{self.project_id}/action", json={"action": "APPROVE"})
        self.assertEqual(res_a.status_code, 200)
        self.assertEqual(res_a.get_json()["new_status"], "APPROVED")

        # 4. Check Queue API
        res_q = self.client.get("/api/queue")
        self.assertEqual(res_q.status_code, 200)
        self.assertIsInstance(res_q.get_json(), list)

if __name__ == "__main__":
    unittest.main()
