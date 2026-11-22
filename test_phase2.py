"""
GameClips AI - Phase 2 Verification Test Suite
Tests:
- Research Agent: topic discovery, claim classification, speculation flagging, duplicate detection
- Footage Discovery Agent: commercial rights verification, rejection of unauthorized sources, catalog population
- Phase 2 Flask API Endpoints
"""

import os
import sys
import unittest
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database, get_connection
from research_agent import calculate_similarity, classify_claims, run_research_cycle, get_topic_evidence_report
from footage_agent import verify_asset_rights, populate_initial_footage_catalog, search_assets_for_topic
from app import app

class TestPhase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.client = app.test_client()

    def test_01_duplicate_detection(self):
        """Verify Jaccard text similarity detects duplicate topics."""
        t1 = "GTA 6 Vice City Map Size Breakdown and Comparisons"
        t2 = "GTA 6 Vice City Map Size Analysis and Breakdown"
        t3 = "Minecraft Nether Update Netherite Armor Crafting"

        sim_dup = calculate_similarity(t1, t2)
        sim_diff = calculate_similarity(t1, t3)

        self.assertGreater(sim_dup, 0.45, "Should identify high similarity for duplicate topic phrasing")
        self.assertLess(sim_diff, 0.1, "Should identify low similarity for distinct topic")

    def test_02_claim_classification(self):
        """Verify speculation markers are accurately flagged and not marked as verified facts."""
        fact_text = "Rockstar Games officially released Trailer 1 on December 5, 2023."
        spec_text = "Unconfirmed insider rumor suggests an alleged delay to 2027."

        fact_res = classify_claims(fact_text)
        self.assertEqual(fact_res["is_verified"], 1)
        self.assertEqual(fact_res["is_speculation"], 0)
        self.assertEqual(fact_res["claim_type"], "VERIFIED_FACT")

        spec_res = classify_claims(spec_text)
        self.assertEqual(spec_res["is_verified"], 0)
        self.assertEqual(spec_res["is_speculation"], 1)
        self.assertEqual(spec_res["claim_type"], "SPECULATION")

    def test_03_research_cycle_execution(self):
        """Verify research cycle discovers topics, sources, and claims in SQLite."""
        result = run_research_cycle("game-gta6")
        self.assertTrue(result["success"])
        self.assertIn("topics_discovered", result)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM topics WHERE game_id = 'game-gta6'")
        topics_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM research_sources WHERE game_id = 'game-gta6'")
        sources_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM factual_claims")
        claims_count = cur.fetchone()[0]
        conn.close()

        self.assertGreaterEqual(topics_count, 3, "Should have discovered topics for GTA 6")
        self.assertGreaterEqual(sources_count, 1, "Should record traceable sources")
        self.assertGreaterEqual(claims_count, 1, "Should record verified claims")

    def test_04_topic_evidence_report(self):
        """Verify topic evidence retrieval returns sources, claims, and speculation count."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        row = cur.fetchone()
        conn.close()

        if row:
            topic_id = row[0]
            report = get_topic_evidence_report(topic_id)
            self.assertIsNotNone(report)
            self.assertIn("topic", report)
            self.assertIn("sources", report)
            self.assertIn("claims", report)

    def test_05_footage_rights_verification(self):
        """Verify rights verification rules strictly approve free commercial and reject unauthorized assets."""
        # 1. Pexels commercial asset
        pexels_asset = {
            "source_platform": "Pexels",
            "source_url": "https://www.pexels.com/video/neon-lighted-city-3129671/",
            "license_name": "Pexels License",
            "commercial_permission": 1
        }
        res_pexels = verify_asset_rights(pexels_asset)
        self.assertEqual(res_pexels["rights_status"], "VERIFIED")
        self.assertEqual(res_pexels["risk_level"], "LOW")

        # 2. Original Vector Visual
        vector_asset = {
            "source_platform": "Original Visuals",
            "source_url": "local://assets/graphics/map.svg",
            "license_name": "Original Clean Vector",
            "commercial_permission": 1
        }
        res_vector = verify_asset_rights(vector_asset)
        self.assertEqual(res_vector["rights_status"], "VERIFIED")

        # 3. Direct YouTube rip (Strictly Prohibited)
        yt_asset = {
            "source_platform": "YouTube",
            "source_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "license_name": "Standard YouTube License",
            "commercial_permission": 0
        }
        res_yt = verify_asset_rights(yt_asset)
        self.assertEqual(res_yt["rights_status"], "REJECTED")
        self.assertEqual(res_yt["risk_level"], "HIGH")

        # 4. Non-commercial license
        nc_asset = {
            "source_platform": "SomeSite",
            "source_url": "https://somesite.com/footage.mp4",
            "license_name": "Creative Commons Non-Commercial",
            "commercial_permission": 0
        }
        res_nc = verify_asset_rights(nc_asset)
        self.assertEqual(res_nc["rights_status"], "REJECTED")

    def test_06_footage_catalog_seeding(self):
        """Verify seeding footage populates rights-verified assets in SQLite."""
        seed_res = populate_initial_footage_catalog("game-gta6")
        self.assertIn("total_catalog_size", seed_res)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM footage_assets WHERE rights_status = 'VERIFIED'")
        verified_count = cur.fetchone()[0]
        conn.close()

        self.assertGreaterEqual(verified_count, 4, "Should have verified assets in the catalog")

    def test_07_footage_keyword_search(self):
        """Verify searching assets by topic keywords returns matched verified assets."""
        results = search_assets_for_topic(["city", "neon", "vice"], "game-gta6")
        self.assertIsInstance(results, list)
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["rights_status"], "VERIFIED")

    def test_08_api_research_endpoints(self):
        """Verify Flask API routes for research trigger and topic evidence."""
        # Run research API
        res = self.client.post("/api/research/run", json={"game_id": "game-gta6"})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])

        # Topic evidence API
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM topics WHERE game_id = 'game-gta6' LIMIT 1")
        topic_id = cur.fetchone()[0]
        conn.close()

        res_ev = self.client.get(f"/api/research/topic/{topic_id}/evidence")
        self.assertEqual(res_ev.status_code, 200)
        self.assertTrue(res_ev.get_json()["success"])

    def test_09_api_footage_endpoints(self):
        """Verify Flask API routes for footage listing, seeding, verification, and registration."""
        # 1. Seed footage
        res_seed = self.client.post("/api/footage/seed")
        self.assertEqual(res_seed.status_code, 200)

        # 2. List footage
        res_list = self.client.get("/api/footage")
        self.assertEqual(res_list.status_code, 200)
        assets = res_list.get_json()
        self.assertGreaterEqual(len(assets), 4)

        # 3. Verify rights API
        audit_payload = {
            "source_platform": "Pixabay",
            "source_url": "https://pixabay.com/videos/street-1234/",
            "license_name": "Pixabay Content License",
            "commercial_permission": 1
        }
        res_audit = self.client.post("/api/footage/verify", json=audit_payload)
        self.assertEqual(res_audit.status_code, 200)
        self.assertEqual(res_audit.get_json()["audit"]["rights_status"], "VERIFIED")

        # 4. Add user asset API
        new_asset = {
            "asset_name": "Test Verified Downtown B-Roll",
            "source_platform": "Pexels",
            "source_url": "https://www.pexels.com/video/downtown-999/",
            "license_name": "Pexels License",
            "commercial_permission": 1,
            "attribution_required": 0
        }
        res_add = self.client.post("/api/footage/add", json=new_asset)
        self.assertEqual(res_add.status_code, 200)
        self.assertTrue(res_add.get_json()["success"])
        self.assertEqual(res_add.get_json()["rights_status"], "VERIFIED")

if __name__ == "__main__":
    unittest.main()
