"""
GameClips AI - Scene Variety & Storytelling Test Suite
Verifies:
1. Comprehensive activity catalog across all 4 major groups.
2. One Video = One Main Topic = One Complete Story rule enforcement.
3. Intelligent non-repetitive selection across Facts & Secrets, Cars & Comparisons, and Stories & Lore.
4. Complete 7-point narrative and visual continuity for all activity blueprints.
"""

import unittest
from scene_library import (
    ACTIVITY_REGISTRY,
    get_all_activities,
    get_activity_by_id,
    select_intelligent_daily_activities
)
from script_generator import generate_script_for_topic
from verification_engine import verify_project_compliance

class TestSceneVariety(unittest.TestCase):
    def test_01_activity_catalog_coverage(self):
        """Verify all 4 required groups have rich, valid activity blueprints."""
        activities = get_all_activities()
        self.assertGreaterEqual(len(activities), 7)

        groups = {act["group"] for act in activities.values()}
        self.assertIn("Walking & Exploration", groups)
        self.assertIn("Vehicles & Transportation", groups)
        self.assertIn("Lifestyle & Entertainment", groups)
        self.assertIn("Action & Adventure", groups)

    def test_02_single_topic_complete_story_structure(self):
        """Verify every activity adheres to: One Video = One Topic = One Complete Story."""
        for act_id, act in ACTIVITY_REGISTRY.items():
            # Mandatory blueprint fields
            self.assertTrue(act.get("title"), f"Activity {act_id} missing title")
            self.assertTrue(act.get("location"), f"Activity {act_id} missing location")
            self.assertTrue(act.get("characters"), f"Activity {act_id} missing characters")
            self.assertTrue(act.get("central_event"), f"Activity {act_id} missing central_event")
            self.assertTrue(act.get("narrative_arc"), f"Activity {act_id} missing narrative_arc")
            self.assertTrue(act.get("resolution"), f"Activity {act_id} missing resolution")

            scenes = act.get("scenes", [])
            self.assertEqual(len(scenes), 6, f"Activity {act_id} must have exactly 6 connected scenes")

            # Check scene continuity linkages
            for sc in scenes:
                self.assertIn("narration_text", sc)
                self.assertIn("camera_movement", sc)
                self.assertTrue(sc.get("prev_scene_connection") or sc["scene_number"] == 1)
                self.assertTrue(sc.get("next_scene_connection") or sc["scene_number"] == 6)

    def test_03_intelligent_daily_activity_selection(self):
        """Verify daily selection picks exactly 3 distinct categories with zero group overlap."""
        plan = select_intelligent_daily_activities()
        self.assertEqual(len(plan), 3)

        categories = [p["category"] for p in plan]
        self.assertEqual(sorted(categories), ["Cars & Comparisons", "Facts & Secrets", "Stories & Lore"])

        # Check that activities and groups are completely distinct
        activity_ids = [p["activity"]["id"] for p in plan]
        self.assertEqual(len(set(activity_ids)), 3, "Activities must be completely distinct")

        groups = [p["activity"]["group"] for p in plan]
        self.assertEqual(len(set(groups)), 3, "Activity groups must be distinct across daily production")

    def test_04_script_generation_and_continuity_audit_all_categories(self):
        """Verify script generation and 100% 7-point continuity across all 3 categories."""
        plan = select_intelligent_daily_activities()
        for item in plan:
            cat = item["category"]
            act = item["activity"]
            act_id = act["id"]
            topic_id = f"test-top-{act_id}"

            # Generate script
            res = generate_script_for_topic("top-daily-facts-and-secrets", activity_id=act_id)
            self.assertTrue(res["success"], f"Failed to generate script for {act_id}")

            proj_id = res["project_id"]
            sb = res["storyboard"]
            self.assertEqual(sb["activity_type"], act_id)

            # Audit compliance & continuity
            v_rep = verify_project_compliance(proj_id)
            cont = v_rep.get("continuity", {})
            self.assertEqual(cont.get("passed_checks"), 7, f"Activity {act_id} failed continuity checks: {cont}")
            self.assertEqual(cont.get("score"), 100.0, f"Activity {act_id} did not get 100% continuity score")

if __name__ == "__main__":
    unittest.main()
