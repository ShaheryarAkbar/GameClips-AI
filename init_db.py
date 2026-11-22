"""
GameClips AI - Database Initialization CLI
Ensures all 14 SQLite tables, WAL mode, foreign keys, and multi-game seeds are initialized.
"""
import sys
from database import init_database

if __name__ == "__main__":
    init_database()
    print("[OK] GameClips AI SQLite database initialized successfully.")
    sys.exit(0)
