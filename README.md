# GameClips AI — Free Local-First Gaming Content Automation

[![GitHub Repo](https://img.shields.io/badge/GitHub-ShaheryarAkbar%2FGameClips--AI-blue?logo=github)](https://github.com/ShaheryarAkbar/GameClips-AI)
[![Tests Passing](https://img.shields.io/badge/Tests-38%2F38%20Passing-brightgreen)](https://github.com/ShaheryarAkbar/GameClips-AI)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](https://github.com/ShaheryarAkbar/GameClips-AI)

**Repository Link:** [https://github.com/ShaheryarAkbar/GameClips-AI](https://github.com/ShaheryarAkbar/GameClips-AI)

**GameClips AI** is a lightweight, local-first gaming content research, script generation, and video production automation engine designed for YouTube Shorts and TikTok.

---

## ⚡ Key Highlights & Core Guarantees

1. **100% Free & Offline-Ready:** Zero paid APIs, no subscriptions, no credit card requirements, no trial paywalls.
2. **Total Privacy:** Never accesses personal Gmail, private files, platform accounts, or credentials.
3. **Mandatory Human Approval Gate:** Candidate videos are never published automatically. Every video requires explicit human sign-off (`APPROVE` / `REJECT` / `REGENERATE`).
4. **Zero Leaked Footage:** Strictly prohibits unauthorized leaked or pirated GTA footage.
5. **Anti-Misrepresentation:** Procedural vector animations are clearly labeled as explanatory/educational graphics and never represented as official leaked GTA 6 gameplay.
6. **Ultra-Lightweight & Hardware-Optimized:**
   - Designed for low-end hardware (tested on Intel Core i5-3427U @ 1.80GHz, 8 GB RAM, Intel HD Graphics 4000).
   - CPU-only FFmpeg H.264 encoding with `-preset ultrafast` renders a vertical short in under 2 seconds (4.5x real-time speed).
   - Total workspace footprint is under **85 MB**.

---

## 🚀 One-Click Launch Instructions

### 1. Launch the Application
In PowerShell, navigate to the project directory and run:
```powershell
.\run.ps1
```
Or directly with the virtual environment Python:
```powershell
.\.venv\Scripts\python.exe app.py
```
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### 2. Run All Automated Test Suites
To verify all 38 unit and integration tests across Phases 1 through 6:
```powershell
.\.venv\Scripts\python.exe -c "
import unittest, sys
loader = unittest.TestLoader()
suite = unittest.TestSuite()
for t in ['test_phase1.py', 'test_phase2.py', 'test_phase3.py', 'test_phase4.py', 'test_phase5.py', 'test_phase6.py']:
    suite.addTests(loader.loadTestsFromModule(__import__(t[:-3])))
runner = unittest.TextTestRunner(verbosity=2)
if not runner.run(suite).wasSuccessful(): sys.exit(1)
"
```

---

## 🖥️ System Architecture & Phase Breakdown

```
+---------------------------------------------------------------------------------------------------+
| PHASE   | COMPONENT                   | DELIVERABLES & VERIFIED CAPABILITIES                              |
+---------------------------------------------------------------------------------------------------+
| Phase 1 | Core & Multi-Game Engine    | SQLite WAL database (14 tables), 8 pre-seeded games, disk monitor |
| Phase 2 | Research & Footage Agent    | Public RSS/web parser, duplicate topic detection, license audit   |
| Phase 3 | Script & Visual Studio      | 30-50s & 60-90s scripts, 9:16 vertical vector frame renderer       |
| Phase 4 | Audio, Subtitles & FFmpeg   | Windows SAPI offline TTS (David/Zira), SRT/ASS subs, MP4 concat   |
| Phase 5 | Rights Audit & Approval     | 8-point copyright compliance check, human sign-off, metadata edit |
| Phase 6 | Export Center & Automation  | Self-contained release packages, analytics, scheduled generation  |
| Phase 7 | Scene Variety & Storytelling| GTA 6 Activity Library (Walking, Vehicles, Lifestyle, Action)     |
+---------------------------------------------------------------------------------------------------+
```

---

## 🎬 GTA 6 Activity & Scene Library (Diverse Storytelling)

To ensure daily productions never become repetitive or overly focused on car driving, the system features an intelligent Activity Library:

- **Group A: Walking & Exploration:**
  - Escobar International Airport terminal exploration (luggage carousels, security gates, tarmac access).
  - Vice Beach oceanfront walks (granular sand displacement, wave foam, sunbathers, wildlife).
  - Luxury hotels & penthouses (grand marble lobbies, glass elevators, private infinity terraces).
  - Neighborhoods & shopping districts (commercial storefronts, crowd density AI, living sidewalks).
- **Group B: Vehicles & Transportation:**
  - High-performance superbikes (Pegassi Bati 801, counter-steering lean physics, 200+ MPH weaving).
  - Heavy 4x4 off-road trucks (Vapid Sandking, mud bog displacement, long-travel suspension, sand dunes).
  - Aviation & aircraft flight (runway takeoff roll, volumetric 3D cloud decks, high-altitude city views).
- **Group C: Lifestyle & Entertainment:**
  - Neon nightclubs & music venues (Club Babylon, synchronized lasers, reactive dancing crowd AI).
  - Resort luxury & beach culture (oceanfront recreation, sunset overlooks, cabana relaxation).
- **Group D: Action & Adventure:**
  - Tactical bank robbery stories (vault thermal drilling, hostage control, duffel bag cash grab).
  - High-speed police pursuits (cruiser boxing formations, spike strips, helicopter searchlights, PIT evasion).

### 📐 Mandatory Storytelling Law: One Video = One Main Topic = One Complete Story
Every video is strictly dedicated to **one central activity and connected narrative arc**. Scene variety exists *between* different daily videos across categories—never by chaotically mixing unrelated activities into a single video.

---

## 📁 Export Package Structure

Approved videos are exported into self-contained release packages organized by release date and category under `exports/<game_slug>/<YYYY-MM-DD>/<category_slug>/<project_slug>_<timestamp>/`:

```
exports/gta-6/2026-11-25/cars-and-comparisons/Grand_Theft_Auto_VI_-_Vice_Cit_20261125_122212/
│
├── final_video.mp4               # Full 1080x1920 9:16 vertical video (H.264 + AAC, 60fps)
├── thumbnail.png                 # High-resolution video thumbnail
├── Title.txt                     # Clean video title
├── Description.txt               # Full video description with citations
├── Hashtags.txt                  # Comma-separated and hash-tagged keywords
├── Sources.txt                   # Complete breakdown of every factual source & URL
├── Copyright_Report.txt          # 8-point legal audit report & disclaimer
│
├── youtube_package/              # YouTube Shorts distribution package
│   ├── yt_title.txt              # Title formatted for Shorts (< 60 chars)
│   ├── yt_description.txt        # Description, chapters, citations, disclaimer
│   └── yt_tags.txt               # Tag list for YouTube Studio
│
└── tiktok_package/               # TikTok distribution package
    ├── tiktok_caption.txt        # Short punchy caption + hashtags (< 150 chars)
    └── tiktok_tags.txt           # Trending TikTok hashtags
```

---

## 🛡️ Mandatory Legal Disclaimer
*Automated detection and verification checks do not guarantee 100% legal immunity or copyright clearance under international intellectual property laws. All generated videos require human review and approval prior to publication.*
