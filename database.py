"""
GameClips AI - Database Module
Local-First SQLite Database Engine with Multi-Game Support and Strict Integrity
"""

import sqlite3
import json
import os
from datetime import datetime

DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_PATH = os.path.join(DB_DIR, "gameclips.db")

def get_connection():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn

def init_database():
    """Initializes all SQLite database tables with full multi-game schema."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = get_connection()
    cur = conn.cursor()

    # 1. Games Table (Modular Multi-Game Architecture)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        slug TEXT NOT NULL UNIQUE,
        description TEXT,
        developer TEXT,
        publisher TEXT,
        official_sources TEXT,
        fan_content_policy_url TEXT,
        commercial_rules TEXT,
        approved_footage_sources TEXT,
        restricted_rules TEXT,
        supported_categories TEXT,
        research_config TEXT,
        is_active INTEGER DEFAULT 0,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    # 2. Topics Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id TEXT PRIMARY KEY,
        game_id TEXT NOT NULL,
        category TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        relevance_score REAL DEFAULT 0.0,
        status TEXT DEFAULT 'DISCOVERED',
        is_duplicate INTEGER DEFAULT 0,
        duplicate_of_id TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
    )
    """)

    # 3. Research Sources
    cur.execute("""
    CREATE TABLE IF NOT EXISTS research_sources (
        id TEXT PRIMARY KEY,
        topic_id TEXT,
        game_id TEXT NOT NULL,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        source_name TEXT NOT NULL,
        author TEXT,
        published_at TEXT,
        reliability_score REAL DEFAULT 0.8,
        notes TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE SET NULL,
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
    )
    """)

    # 4. Factual Claims
    cur.execute("""
    CREATE TABLE IF NOT EXISTS factual_claims (
        id TEXT PRIMARY KEY,
        topic_id TEXT NOT NULL,
        claim_text TEXT NOT NULL,
        is_verified INTEGER DEFAULT 0,
        evidence_source_id TEXT,
        is_speculation INTEGER DEFAULT 0,
        claim_type TEXT DEFAULT 'OFFICIAL',
        created_at TEXT NOT NULL,
        FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE,
        FOREIGN KEY (evidence_source_id) REFERENCES research_sources(id) ON DELETE SET NULL
    )
    """)

    # 5. Scripts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS scripts (
        id TEXT PRIMARY KEY,
        topic_id TEXT,
        game_id TEXT NOT NULL,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        target_duration TEXT DEFAULT '30-50s',
        hook TEXT NOT NULL,
        body TEXT NOT NULL,
        closing TEXT NOT NULL,
        voiceover_text TEXT NOT NULL,
        full_script TEXT,
        scene_count INTEGER DEFAULT 3,
        hashtags TEXT,
        youtube_title TEXT,
        youtube_description TEXT,
        tiktok_caption TEXT,
        status TEXT DEFAULT 'DRAFT',
        created_at TEXT NOT NULL,
        FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE SET NULL,
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
    )
    """)

    # 6. Video Projects
    cur.execute("""
    CREATE TABLE IF NOT EXISTS video_projects (
        id TEXT PRIMARY KEY,
        script_id TEXT NOT NULL,
        game_id TEXT NOT NULL,
        project_name TEXT NOT NULL,
        status TEXT DEFAULT 'PENDING',
        target_resolution TEXT DEFAULT '1080x1920',
        aspect_ratio TEXT DEFAULT '9:16',
        fps INTEGER DEFAULT 30,
        quality_preset TEXT DEFAULT 'ultrafast',
        duration_seconds REAL DEFAULT 0.0,
        preview_path TEXT,
        final_video_path TEXT,
        thumbnail_path TEXT,
        error_message TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        FOREIGN KEY (script_id) REFERENCES scripts(id) ON DELETE CASCADE,
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
    )
    """)

    # 7. Video Scenes
    cur.execute("""
    CREATE TABLE IF NOT EXISTS video_scenes (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL,
        scene_number INTEGER NOT NULL,
        start_time REAL NOT NULL,
        end_time REAL NOT NULL,
        visual_type TEXT DEFAULT 'SVG_ANIMATION',
        visual_prompt TEXT,
        visual_asset_path TEXT,
        narration_text TEXT,
        subtitle_text TEXT,
        transition_type TEXT DEFAULT 'fade',
        location TEXT,
        character_focus TEXT,
        vehicle TEXT,
        camera_movement TEXT,
        action_progression TEXT,
        prev_scene_connection TEXT,
        next_scene_connection TEXT,
        is_fictional INTEGER DEFAULT 0,
        continuity_verified INTEGER DEFAULT 1,
        created_at TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES video_projects(id) ON DELETE CASCADE
    )
    """)

    # 7b. Storyboards Table (Mandatory Narrative & Visual Continuity System)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS storyboards (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL,
        script_id TEXT NOT NULL,
        story_title TEXT NOT NULL,
        main_characters TEXT NOT NULL,
        vehicle TEXT,
        environment_location TEXT NOT NULL,
        time_of_day TEXT NOT NULL,
        weather TEXT NOT NULL,
        central_event TEXT NOT NULL,
        narrative_arc TEXT NOT NULL,
        resolution TEXT NOT NULL,
        continuity_score REAL DEFAULT 100.0,
        continuity_status TEXT DEFAULT 'VALIDATED',
        created_at TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES video_projects(id) ON DELETE CASCADE,
        FOREIGN KEY (script_id) REFERENCES scripts(id) ON DELETE CASCADE
    )
    """)

    # 8. Footage Assets
    cur.execute("""
    CREATE TABLE IF NOT EXISTS footage_assets (
        id TEXT PRIMARY KEY,
        game_id TEXT NOT NULL,
        asset_name TEXT NOT NULL,
        source_platform TEXT NOT NULL,
        source_url TEXT NOT NULL,
        asset_url TEXT NOT NULL,
        author_name TEXT,
        license_name TEXT NOT NULL,
        license_url TEXT NOT NULL,
        commercial_permission INTEGER DEFAULT 0,
        attribution_required INTEGER DEFAULT 0,
        local_path TEXT,
        rights_status TEXT DEFAULT 'UNKNOWN',
        file_size_mb REAL DEFAULT 0.0,
        download_date TEXT NOT NULL,
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
    )
    """)

    # 9. Asset Licenses
    cur.execute("""
    CREATE TABLE IF NOT EXISTS asset_licenses (
        id TEXT PRIMARY KEY,
        asset_id TEXT NOT NULL,
        license_name TEXT NOT NULL,
        license_text TEXT,
        can_commercial INTEGER DEFAULT 0,
        can_modify INTEGER DEFAULT 1,
        attribution_notice TEXT,
        verified_at TEXT NOT NULL,
        verifier_notes TEXT,
        FOREIGN KEY (asset_id) REFERENCES footage_assets(id) ON DELETE CASCADE
    )
    """)

    # 10. Audio Assets
    cur.execute("""
    CREATE TABLE IF NOT EXISTS audio_assets (
        id TEXT PRIMARY KEY,
        project_id TEXT,
        audio_type TEXT DEFAULT 'TTS',
        voice_name TEXT DEFAULT 'Microsoft David Desktop',
        file_path TEXT NOT NULL,
        duration_seconds REAL DEFAULT 0.0,
        sample_rate INTEGER DEFAULT 44100,
        license_status TEXT DEFAULT 'SYSTEM_OFFLINE_FREE',
        created_at TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES video_projects(id) ON DELETE SET NULL
    )
    """)

    # 11. Verification Reports
    cur.execute("""
    CREATE TABLE IF NOT EXISTS verification_reports (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL UNIQUE,
        asset_license_status TEXT DEFAULT 'UNKNOWN',
        rights_traceability_status TEXT DEFAULT 'UNKNOWN',
        duplicate_usage_flag INTEGER DEFAULT 0,
        fact_verification_status TEXT DEFAULT 'UNVERIFIED',
        copyright_risk_level TEXT DEFAULT 'LOW',
        status TEXT DEFAULT 'NEEDS_REVIEW',
        warning_notes TEXT,
        disclaimer_notice TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES video_projects(id) ON DELETE CASCADE
    )
    """)

    # 12. Approval History
    cur.execute("""
    CREATE TABLE IF NOT EXISTS approval_history (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL,
        action TEXT NOT NULL,
        reviewer_notes TEXT,
        rights_warning_acknowledged INTEGER DEFAULT 0,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES video_projects(id) ON DELETE CASCADE
    )
    """)

    # 13. Exported Videos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exported_videos (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL UNIQUE,
        game_id TEXT NOT NULL,
        export_folder TEXT NOT NULL,
        video_path TEXT NOT NULL,
        thumbnail_path TEXT,
        youtube_package_path TEXT,
        tiktok_package_path TEXT,
        export_timestamp TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES video_projects(id) ON DELETE CASCADE,
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
    )
    """)

    # 14. System Settings
    cur.execute("""
    CREATE TABLE IF NOT EXISTS system_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL,
        description TEXT,
        category TEXT DEFAULT 'GENERAL',
        updated_at TEXT NOT NULL
    )
    """)

    # 15. Automated Schema Migration for Storyboard & Continuity
    cur.execute("PRAGMA table_info(video_scenes)")
    scene_cols = [r[1] for r in cur.fetchall()]
    new_scene_fields = [
        ("location", "TEXT"),
        ("character_focus", "TEXT"),
        ("vehicle", "TEXT"),
        ("camera_movement", "TEXT"),
        ("action_progression", "TEXT"),
        ("prev_scene_connection", "TEXT"),
        ("next_scene_connection", "TEXT"),
        ("is_fictional", "INTEGER DEFAULT 0"),
        ("continuity_verified", "INTEGER DEFAULT 1")
    ]
    for col_name, col_def in new_scene_fields:
        if col_name not in scene_cols:
            try:
                cur.execute(f"ALTER TABLE video_scenes ADD COLUMN {col_name} {col_def}")
            except Exception:
                pass

    cur.execute("PRAGMA table_info(verification_reports)")
    vrf_cols = [r[1] for r in cur.fetchall()]
    new_vrf_fields = [
        ("continuity_status", "TEXT DEFAULT 'VERIFIED'"),
        ("continuity_score", "REAL DEFAULT 100.0"),
        ("continuity_details", "TEXT")
    ]
    for col_name, col_def in new_vrf_fields:
        if col_name not in vrf_cols:
            try:
                cur.execute(f"ALTER TABLE verification_reports ADD COLUMN {col_name} {col_def}")
            except Exception:
                pass

    conn.commit()

    conn.commit()
    seed_initial_data(conn)
    conn.close()
    print("[OK] Database initialized successfully.")

def seed_initial_data(conn):
    """Populates initial modular game library and system settings."""
    cur = conn.cursor()
    now = datetime.now().isoformat()

    # Initial Game Library (GTA 6 active, others ready)
    initial_games = [
        {
            "id": "game-gta6",
            "name": "Grand Theft Auto VI",
            "slug": "gta-6",
            "description": "Next-generation open world action-adventure game set in Leonida (Vice City) by Rockstar Games.",
            "developer": "Rockstar Studios",
            "publisher": "Take-Two Interactive / Rockstar Games",
            "official_sources": json.dumps([
                "https://www.rockstargames.com/VI",
                "https://www.rockstargames.com/newswire",
                "https://twitter.com/RockstarGames"
            ]),
            "fan_content_policy_url": "https://support.rockstargames.com/articles/200153756/Policy-on-posting-copyrighted-Rockstar-Games-material",
            "commercial_rules": "Strict Non-Commercial & Fan Policy: No monetization of raw unedited footage. Factual educational/commentary allowed with original transformation. Leaked gameplay strictly prohibited.",
            "approved_footage_sources": json.dumps(["Pexels", "Pixabay", "Mixkit", "Original SVG/CSS Graphics"]),
            "restricted_rules": json.dumps([
                "Never use leaked or pirated footage.",
                "Never misrepresent mockups/renders as official gameplay.",
                "Always label speculative content clearly."
            ]),
            "supported_categories": json.dumps([
                "Facts & Secrets",
                "Cars & Comparisons",
                "Stories & Theories",
                "Characters",
                "Hidden Details"
            ]),
            "research_config": json.dumps({
                "rss_feeds": [
                    "https://www.rockstargames.com/newswire.rss"
                ],
                "search_keywords": ["GTA 6", "Grand Theft Auto VI", "Vice City Leonida", "Rockstar Games GTA VI"],
                "max_daily_candidates": 3
            }),
            "is_active": 1
        },
        {
            "id": "game-gta5",
            "name": "Grand Theft Auto V",
            "slug": "gta-5",
            "description": "Iconic open-world crime epic set in Los Santos and Blaine County.",
            "developer": "Rockstar North",
            "publisher": "Rockstar Games",
            "official_sources": json.dumps(["https://www.rockstargames.com/gta-v"]),
            "fan_content_policy_url": "https://support.rockstargames.com/articles/200153756/Policy-on-posting-copyrighted-Rockstar-Games-material",
            "commercial_rules": "Commentary & transformative content permitted under fan video policy.",
            "approved_footage_sources": json.dumps(["Original Visuals", "Verified Free Assets"]),
            "restricted_rules": json.dumps(["No copyright music", "No raw unedited cinematic uploads"]),
            "supported_categories": json.dumps(["Facts & Secrets", "Cars & Comparisons", "Hidden Details", "Lore"]),
            "research_config": json.dumps({"search_keywords": ["GTA 5 facts", "Los Santos secrets"]}),
            "is_active": 0
        },
        {
            "id": "game-gta4",
            "name": "Grand Theft Auto IV",
            "slug": "gta-4",
            "description": "Gritty Liberty City story of Niko Bellic exploring the American Dream.",
            "developer": "Rockstar North",
            "publisher": "Rockstar Games",
            "official_sources": json.dumps(["https://www.rockstargames.com/games/IV"]),
            "fan_content_policy_url": "https://support.rockstargames.com",
            "commercial_rules": "Educational commentary / analysis permitted under fair-use/fan guidelines.",
            "approved_footage_sources": json.dumps(["Original Visuals", "Free B-Roll"]),
            "restricted_rules": json.dumps(["No radio station music tracks"]),
            "supported_categories": json.dumps(["Facts & Secrets", "Physics Comparison", "Lore & Stories"]),
            "research_config": json.dumps({"search_keywords": ["GTA 4 physics", "Niko Bellic facts"]}),
            "is_active": 0
        },
        {
            "id": "game-gtasa",
            "name": "Grand Theft Auto: San Andreas",
            "slug": "gta-san-andreas",
            "description": "Legendary early-2000s classic following CJ in Los Santos, San Fierro, and Las Venturas.",
            "developer": "Rockstar North",
            "publisher": "Rockstar Games",
            "official_sources": json.dumps(["https://www.rockstargames.com"]),
            "fan_content_policy_url": "https://support.rockstargames.com",
            "commercial_rules": "Educational & nostalgic retrospectives permitted.",
            "approved_footage_sources": json.dumps(["Original Graphics", "Free Assets"]),
            "restricted_rules": json.dumps(["No in-game copyrighted radio audio"]),
            "supported_categories": json.dumps(["Facts & Secrets", "Myths & Legends", "Hidden Details"]),
            "research_config": json.dumps({"search_keywords": ["GTA San Andreas myths", "CJ facts"]}),
            "is_active": 0
        },
        {
            "id": "game-gtavc",
            "name": "Grand Theft Auto: Vice City",
            "slug": "gta-vice-city",
            "description": "1980s neon-soaked classic featuring Tommy Vercetti.",
            "developer": "Rockstar North",
            "publisher": "Rockstar Games",
            "official_sources": json.dumps(["https://www.rockstargames.com"]),
            "fan_content_policy_url": "https://support.rockstargames.com",
            "commercial_rules": "Commentary permitted without licensed 80s music.",
            "approved_footage_sources": json.dumps(["Original Neon Graphics", "Free B-Roll"]),
            "restricted_rules": json.dumps(["Strictly no commercial 80s soundtrack clips"]),
            "supported_categories": json.dumps(["Facts & Secrets", "80s Lore", "Cars & Comparisons"]),
            "research_config": json.dumps({"search_keywords": ["GTA Vice City secrets", "Tommy Vercetti"]}),
            "is_active": 0
        },
        {
            "id": "game-gta3",
            "name": "Grand Theft Auto III",
            "slug": "gta-3",
            "description": "The revolutionary title that pioneered 3D open-world gaming.",
            "developer": "DMA Design / Rockstar",
            "publisher": "Rockstar Games",
            "official_sources": json.dumps(["https://www.rockstargames.com"]),
            "fan_content_policy_url": "https://support.rockstargames.com",
            "commercial_rules": "Historical / educational retrospectives permitted.",
            "approved_footage_sources": json.dumps(["Original Visuals", "Free B-Roll"]),
            "restricted_rules": json.dumps(["No unedited full cutscenes"]),
            "supported_categories": json.dumps(["Historical Evolution", "Facts & Secrets"]),
            "research_config": json.dumps({"search_keywords": ["GTA 3 development history", "Claude Speed"]}),
            "is_active": 0
        },
        {
            "id": "game-rdr2",
            "name": "Red Dead Redemption 2",
            "slug": "rdr-2",
            "description": "Epic Western masterpiece detailing Arthur Morgan and the Van der Linde gang.",
            "developer": "Rockstar Studios",
            "publisher": "Rockstar Games",
            "official_sources": json.dumps(["https://www.rockstargames.com/reddeadredemption2"]),
            "fan_content_policy_url": "https://support.rockstargames.com",
            "commercial_rules": "Transformative storytelling & details breakdown permitted.",
            "approved_footage_sources": json.dumps(["Original Western Graphics", "Free Wildlife B-Roll"]),
            "restricted_rules": json.dumps(["No uncredited spoilers without tag"]),
            "supported_categories": json.dumps(["Insane Details", "Facts & Secrets", "Lore & Stories"]),
            "research_config": json.dumps({"search_keywords": ["RDR2 attention to detail", "Arthur Morgan secrets"]}),
            "is_active": 0
        },
        {
            "id": "game-minecraft",
            "name": "Minecraft",
            "slug": "minecraft",
            "description": "Global sandbox phenomenon created by Mojang Studios.",
            "developer": "Mojang Studios",
            "publisher": "Xbox Game Studios",
            "official_sources": json.dumps(["https://www.minecraft.net"]),
            "fan_content_policy_url": "https://www.minecraft.net/en-us/usage-guidelines",
            "commercial_rules": "Commercial fan content permitted under Mojang Commercial Usage Guidelines.",
            "approved_footage_sources": json.dumps(["Original Blocky Graphics", "Free Creative Commons Assets"]),
            "restricted_rules": json.dumps(["Do not claim official affiliation", "Do not sell assets"]),
            "supported_categories": json.dumps(["Facts & Secrets", "Build Comparisons", "Game Mechanics", "Lore"]),
            "research_config": json.dumps({"search_keywords": ["Minecraft secrets", "Minecraft facts", "Mojang update"]}),
            "is_active": 0
        }
    ]

    for game in initial_games:
        cur.execute("""
        INSERT OR IGNORE INTO games (
            id, name, slug, description, developer, publisher, official_sources,
            fan_content_policy_url, commercial_rules, approved_footage_sources,
            restricted_rules, supported_categories, research_config, is_active,
            created_at, updated_at
        ) VALUES (
            :id, :name, :slug, :description, :developer, :publisher, :official_sources,
            :fan_content_policy_url, :commercial_rules, :approved_footage_sources,
            :restricted_rules, :supported_categories, :research_config, :is_active,
            :created_at, :updated_at
        )
        """, {**game, "created_at": now, "updated_at": now})

    # Default System Settings (Optimized for Low-End Hardware)
    default_settings = [
        ("target_platform", "YouTube Shorts & TikTok", "Primary target short-form formats", "GENERAL"),
        ("daily_video_target", "3", "Maximum automated video candidates per cycle", "AUTOMATION"),
        ("render_preset", "ultrafast", "FFmpeg CPU encoding speed (ultrafast for i5-3427U)", "VIDEO"),
        ("render_resolution", "1080x1920", "Target 9:16 vertical resolution", "VIDEO"),
        ("render_fps", "30", "Framerate target (30fps recommended for low CPU load)", "VIDEO"),
        ("storage_limit_gb", "2.0", "Maximum disk space for temporary render files", "STORAGE"),
        ("min_disk_headroom_gb", "5.0", "Minimum free disk space required before halting renders", "STORAGE"),
        ("offline_tts_voice", "Microsoft David Desktop", "Windows Native SAPI voice name", "AUDIO"),
        ("auto_cleanup_temp", "true", "Automatically purge temporary renders after export", "STORAGE"),
        ("strict_copyright_check", "true", "Block export if asset license is UNKNOWN or REJECTED", "SECURITY")
    ]

    for key, val, desc, cat in default_settings:
        cur.execute("""
        INSERT OR IGNORE INTO system_settings (key, value, description, category, updated_at)
        VALUES (?, ?, ?, ?, ?)
        """, (key, val, desc, cat, now))

    # Add initial seed topics for GTA 6 across the 3 core categories
    seed_topics = [
        {
            "id": "top-gta6-001",
            "game_id": "game-gta6",
            "category": "Facts & Secrets",
            "title": "Vice City Map Size: 2.5x Bigger Than Los Santos?",
            "description": "Analysis of official Rockstar trailer coordinates and mapping community estimations showing Leonida state geography.",
            "relevance_score": 9.4,
            "status": "APPROVED_TOPIC"
        },
        {
            "id": "top-gta6-002",
            "game_id": "game-gta6",
            "category": "Cars & Comparisons",
            "title": "GTA 6 Vehicle Physics: Confirmed Interior & Suspension Upgrades",
            "description": "Breakdown of confirmed car models, interactive digital dashboards, and dynamic vehicle deformation based on official trailer frames.",
            "relevance_score": 8.9,
            "status": "APPROVED_TOPIC"
        },
        {
            "id": "top-gta6-003",
            "game_id": "game-gta6",
            "category": "Stories",
            "title": "Lucia & Jason: The Modern Bonnie and Clyde Dynamic",
            "description": "Original narrative exploration of protagonist trust mechanics and partner cooperation in the neon criminal underworld.",
            "relevance_score": 9.1,
            "status": "APPROVED_TOPIC"
        }
    ]

    for t in seed_topics:
        cur.execute("""
        INSERT OR IGNORE INTO topics (id, game_id, category, title, description, relevance_score, status, is_duplicate, created_at, updated_at)
        VALUES (:id, :game_id, :category, :title, :description, :relevance_score, :status, 0, :created_at, :updated_at)
        """, {**t, "created_at": now, "updated_at": now})

    conn.commit()

if __name__ == "__main__":
    init_database()
