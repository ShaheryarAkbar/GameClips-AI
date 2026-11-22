"""
GameClips AI - Analytics & Metrics Engine
Aggregates channel/content metrics, production funnel statistics,
copyright compliance ratings, and real-time hardware/storage monitoring.
"""

from database import get_connection
from storage_manager import get_disk_status

def get_analytics_summary() -> dict:
    """
    Computes comprehensive analytics across research, production,
    verification, exports, and hardware storage.
    """
    conn = get_connection()
    cur = conn.cursor()

    try:
        # 1. Topics Overview
        cur.execute("SELECT COUNT(*) FROM topics")
        total_topics = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM topics WHERE is_duplicate = 1")
        duplicate_topics = cur.fetchone()[0]

        cur.execute("""
            SELECT category, COUNT(*) as count
            FROM topics
            GROUP BY category
        """)
        category_counts = {row["category"]: row["count"] for row in cur.fetchall()}

        # 2. Scripts Overview
        cur.execute("SELECT COUNT(*) FROM scripts")
        total_scripts = cur.fetchone()[0]

        # 3. Video Projects Funnel
        cur.execute("SELECT COUNT(*) FROM video_projects")
        total_rendered = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM video_projects WHERE status = 'APPROVED'")
        approved_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM video_projects WHERE status = 'REJECTED'")
        rejected_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM video_projects WHERE status IN ('PENDING', 'NEEDS_REVIEW')")
        pending_review_count = cur.fetchone()[0]

        # 4. Exports Overview
        cur.execute("SELECT COUNT(*) FROM exported_videos")
        total_exported = cur.fetchone()[0]

        # 5. Review Ratios
        total_reviewed = approved_count + rejected_count
        approval_rate = round((approved_count / total_reviewed) * 100, 1) if total_reviewed > 0 else 0.0
        rejection_rate = round((rejected_count / total_reviewed) * 100, 1) if total_reviewed > 0 else 0.0

        # 6. Verification & Rights Compliance Index
        cur.execute("SELECT COUNT(*) FROM verification_reports")
        total_verifications = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM verification_reports WHERE status = 'VERIFIED'")
        verified_compliance = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM verification_reports WHERE status = 'NEEDS_REVIEW'")
        review_compliance = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM verification_reports WHERE status = 'REJECTED'")
        rejected_compliance = cur.fetchone()[0]

        safety_index = round((verified_compliance / total_verifications) * 100, 1) if total_verifications > 0 else 100.0

        # 7. Footage & Asset Library
        cur.execute("SELECT COUNT(*) FROM footage_assets")
        total_assets = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM footage_assets WHERE commercial_permission = 1 AND rights_status = 'VERIFIED'")
        approved_assets = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM footage_assets WHERE rights_status = 'REJECTED' OR commercial_permission = 0")
        rejected_assets = cur.fetchone()[0]

        # 8. Multi-Game Breakdown
        cur.execute("""
            SELECT g.name, g.slug, COUNT(t.id) as topic_count
            FROM games g
            LEFT JOIN topics t ON g.id = t.game_id
            GROUP BY g.id
            ORDER BY topic_count DESC
        """)
        game_breakdown = [dict(row) for row in cur.fetchall()]

        # 9. Recent Approval History Timeline
        cur.execute("""
            SELECT ah.*, p.project_name
            FROM approval_history ah
            JOIN video_projects p ON ah.project_id = p.id
            ORDER BY ah.timestamp DESC
            LIMIT 6
        """)
        recent_decisions = [dict(row) for row in cur.fetchall()]

        # 10. Storage & Hardware Metrics
        disk_metrics = get_disk_status()

        return {
            "funnel": {
                "topics_discovered": total_topics,
                "scripts_generated": total_scripts,
                "videos_rendered": total_rendered,
                "approved": approved_count,
                "rejected": rejected_count,
                "pending_review": pending_review_count,
                "exported": total_exported,
                "approval_rate_percent": approval_rate,
                "rejection_rate_percent": rejection_rate
            },
            "topics": {
                "total": total_topics,
                "duplicates_filtered": duplicate_topics,
                "unique_topics": total_topics - duplicate_topics,
                "by_category": {
                    "facts_and_secrets": category_counts.get("Facts & Secrets", 0),
                    "cars_and_comparisons": category_counts.get("Cars & Comparisons", 0),
                    "stories_and_theories": category_counts.get("Stories", 0)
                }
            },
            "compliance_safety": {
                "total_reports": total_verifications,
                "verified": verified_compliance,
                "needs_review": review_compliance,
                "rejected": rejected_compliance,
                "safety_score_index": safety_index,
                "disclaimer_enforced": True
            },
            "footage_assets": {
                "total": total_assets,
                "approved_commercial": approved_assets,
                "rejected_or_unclear": rejected_assets
            },
            "game_distribution": game_breakdown,
            "recent_activity": recent_decisions,
            "storage": disk_metrics
        }
    finally:
        conn.close()
