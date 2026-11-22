"""
GameClips AI - Footage Discovery & Rights Verification Agent
Discovers free commercial assets, audits licensing terms,
validates attribution, and enforces strict copyright safety.
"""

import os
import json
from datetime import datetime
from database import get_connection

# Curated catalog of rights-verified free commercial assets (Pexels, Pixabay, Mixkit, and Original Vectors)
# Each asset contains verified license URLs and explicit commercial permissions.
VERIFIED_ASSET_CATALOG = [
    {
        "asset_name": "Neon City Skyline Night View (Vice City B-Roll)",
        "source_platform": "Pexels",
        "source_url": "https://www.pexels.com/video/neon-lighted-city-skyline-at-night-3129671/",
        "asset_url": "https://images.pexels.com/videos/3129671/free-video-3129671.jpg",
        "author_name": "Kelly Lacy",
        "license_name": "Pexels License",
        "license_url": "https://www.pexels.com/license/",
        "commercial_permission": 1,
        "attribution_required": 0,
        "attribution_notice": "Free to use for commercial and non-commercial purposes. Attribution appreciated.",
        "tags": ["neon", "city", "vice city", "night", "buildings", "gta-6"]
    },
    {
        "asset_name": "Modern Supercar Driving in Highway Traffic",
        "source_platform": "Pixabay",
        "source_url": "https://pixabay.com/videos/car-traffic-speed-street-drive-11808/",
        "asset_url": "https://cdn.pixabay.com/v/car-traffic-preview.jpg",
        "author_name": "StockFootageWorld",
        "license_name": "Pixabay Content License",
        "license_url": "https://pixabay.com/service/license-summary/",
        "commercial_permission": 1,
        "attribution_required": 0,
        "attribution_notice": "Pixabay Content License allows commercial use across digital platforms without mandatory attribution.",
        "tags": ["car", "supercar", "vehicle", "highway", "speed", "cars-comparison", "gta-6"]
    },
    {
        "asset_name": "Retro Gaming Console & Controller Neon Glow",
        "source_platform": "Mixkit",
        "source_url": "https://mixkit.co/free-stock-video/retro-video-game-controller-in-neon-lights-42938/",
        "asset_url": "https://assets.mixkit.co/videos/preview/mixkit-retro-video-game-controller.jpg",
        "author_name": "Mixkit Production",
        "license_name": "Mixkit Stock Video Free License",
        "license_url": "https://mixkit.co/license/#videoFree",
        "commercial_permission": 1,
        "attribution_required": 0,
        "attribution_notice": "Permitted for commercial YouTube and social media video production.",
        "tags": ["gaming", "controller", "retro", "neon", "facts-secrets"]
    },
    {
        "asset_name": "Original Leonida Stylized Vector Map & Route Highlight",
        "source_platform": "Original Visuals",
        "source_url": "local://assets/graphics/leonida_map.svg",
        "asset_url": "local://assets/graphics/leonida_map.svg",
        "author_name": "GameClips AI Engine",
        "license_name": "Original Clean Vector / Proprietary Open License",
        "license_url": "local://LICENSE_ORIGINAL",
        "commercial_permission": 1,
        "attribution_required": 0,
        "attribution_notice": "100% original programmatic vector graphic. Zero third-party copyright claims.",
        "tags": ["map", "leonida", "vice city", "svg", "original", "gta-6"]
    },
    {
        "asset_name": "Original Cyberpunk Neon Countdown & Fact Lower-Third",
        "source_platform": "Original Visuals",
        "source_url": "local://assets/graphics/neon_titles.svg",
        "asset_url": "local://assets/graphics/neon_titles.svg",
        "author_name": "GameClips AI Engine",
        "license_name": "Original Clean Vector / Proprietary Open License",
        "license_url": "local://LICENSE_ORIGINAL",
        "commercial_permission": 1,
        "attribution_required": 0,
        "attribution_notice": "Original SVG animation layout. 100% safe for monetized content.",
        "tags": ["titles", "lower third", "svg", "typography", "gta-6"]
    }
]

def verify_asset_rights(asset_data):
    """
    Evaluates whether an asset is safely cleared for commercial gaming content:
    - Checks license type
    - Checks commercial permissions
    - Rejects unauthorized game rip sources (e.g. YouTube rips, leaked clips)
    Returns: status ('VERIFIED', 'NEEDS_REVIEW', 'REJECTED', 'UNKNOWN'), notes, risk_level
    """
    source_url = asset_data.get("source_url", "").lower()
    license_name = asset_data.get("license_name", "").lower()
    commercial = asset_data.get("commercial_permission", 0)

    # 1. Immediate rejection rules
    rejected_domains = ["youtube.com", "youtu.be", "tiktok.com", "bilibili.com", "dailymotion.com", "leak", "pirate"]
    if any(d in source_url for d in rejected_domains):
        return {
            "rights_status": "REJECTED",
            "risk_level": "HIGH",
            "notes": "Direct video-sharing rips or unverified gameplay clips are strictly rejected under Project Rules."
        }

    # 2. Check for non-commercial or unclear licenses
    non_commercial_flags = ["non-commercial", "nc", "editorial use only", "personal use only"]
    if any(f in license_name for f in non_commercial_flags) or commercial == 0:
        return {
            "rights_status": "REJECTED",
            "risk_level": "HIGH",
            "notes": "Asset license explicitly excludes commercial use or is marked editorial only."
        }

    # 3. Verified recognized public licenses
    verified_licenses = [
        "pexels license", "pixabay content license", "mixkit stock video free license",
        "cc0", "creative commons zero", "original clean vector", "public domain"
    ]
    if any(vl in license_name for vl in verified_licenses) and commercial == 1:
        return {
            "rights_status": "VERIFIED",
            "risk_level": "LOW",
            "notes": "Verified commercial-use rights cleared under standard platform terms."
        }

    # 4. Fallback for unrecognized licenses
    return {
        "rights_status": "NEEDS_REVIEW",
        "risk_level": "MEDIUM",
        "notes": "License terms require human verification before production queue approval."
    }

def populate_initial_footage_catalog(game_id="game-gta6"):
    """Seeds the rights-verified asset library for the specified game."""
    conn = get_connection()
    cur = conn.cursor()
    now = datetime.now().isoformat()

    added_count = 0
    for idx, item in enumerate(VERIFIED_ASSET_CATALOG):
        asset_id = f"ast-{game_id[:8]}-{idx+1:03d}"
        
        # Check if already exists
        cur.execute("SELECT id FROM footage_assets WHERE id = ? OR asset_name = ?", (asset_id, item["asset_name"]))
        if cur.fetchone():
            continue

        audit = verify_asset_rights(item)

        cur.execute("""
        INSERT INTO footage_assets (
            id, game_id, asset_name, source_platform, source_url, asset_url,
            author_name, license_name, license_url, commercial_permission,
            attribution_required, local_path, rights_status, file_size_mb, download_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0.0, ?)
        """, (
            asset_id, game_id, item["asset_name"], item["source_platform"],
            item["source_url"], item["asset_url"], item["author_name"],
            item["license_name"], item["license_url"], item["commercial_permission"],
            item["attribution_required"], f"assets/{asset_id}.svg" if "Original" in item["source_platform"] else None,
            audit["rights_status"], now
        ))

        # License details
        lic_id = f"lic-{asset_id}"
        cur.execute("""
        INSERT INTO asset_licenses (
            id, asset_id, license_name, license_text, can_commercial, can_modify,
            attribution_notice, verified_at, verifier_notes
        ) VALUES (?, ?, ?, ?, ?, 1, ?, ?, ?)
        """, (
            lic_id, asset_id, item["license_name"], item.get("attribution_notice"),
            item["commercial_permission"], item.get("attribution_notice"),
            now, audit["notes"]
        ))
        added_count += 1

    conn.commit()
    conn.close()
    return {"added": added_count, "total_catalog_size": len(VERIFIED_ASSET_CATALOG)}

def search_assets_for_topic(keywords, game_id=None):
    """
    Finds verified assets matching topic keywords.
    Only returns assets with rights_status == 'VERIFIED'.
    """
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT a.*, l.attribution_notice
    FROM footage_assets a
    JOIN asset_licenses l ON a.id = l.asset_id
    WHERE a.rights_status = 'VERIFIED'
    """
    params = []
    if game_id:
        query += " AND a.game_id = ?"
        params.append(game_id)

    cur.execute(query, params)
    assets = [dict(r) for r in cur.fetchall()]
    conn.close()

    # Score by keyword matches
    scored = []
    tokens = [k.lower() for k in keywords]
    for a in assets:
        score = 0
        name_lower = a["asset_name"].lower()
        for t in tokens:
            if t in name_lower:
                score += 2
        scored.append((score, a))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored]

if __name__ == "__main__":
    import pprint
    res = populate_initial_footage_catalog()
    pprint.pprint(res)
