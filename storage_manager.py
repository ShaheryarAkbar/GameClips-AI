"""
GameClips AI - Storage Management Engine
Monitors disk space, controls render cache, purges temporary files,
and guarantees low-end hardware protection.
"""

import os
import shutil
import hashlib
from datetime import datetime
from database import get_connection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp_render")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DATA_DIR = os.path.join(BASE_DIR, "data")

def ensure_directories():
    """Ensure all required project storage directories exist."""
    for d in [TEMP_DIR, EXPORTS_DIR, DATA_DIR]:
        os.makedirs(d, exist_ok=True)

def get_disk_status():
    """
    Returns current disk space metrics for the project drive (E:)
    and the operating system drive (C:).
    """
    ensure_directories()
    metrics = {}

    # Check project workspace drive (e.g., E:)
    drive_path = os.path.splitdrive(BASE_DIR)[0] + "\\"
    try:
        total, used, free = shutil.disk_usage(drive_path)
        metrics["project_drive"] = {
            "drive": drive_path,
            "total_gb": round(total / (1024**3), 2),
            "used_gb": round(used / (1024**3), 2),
            "free_gb": round(free / (1024**3), 2),
            "free_percent": round((free / total) * 100, 1)
        }
    except Exception as e:
        metrics["project_drive"] = {"error": str(e)}

    # Check OS drive (C:)
    try:
        c_total, c_used, c_free = shutil.disk_usage("C:\\")
        metrics["os_drive"] = {
            "drive": "C:\\",
            "total_gb": round(c_total / (1024**3), 2),
            "used_gb": round(c_used / (1024**3), 2),
            "free_gb": round(c_free / (1024**3), 2),
            "free_percent": round((c_free / c_total) * 100, 1)
        }
    except Exception as e:
        metrics["os_drive"] = {"error": str(e)}

    # Measure temp render directory size
    temp_size_bytes = 0
    temp_file_count = 0
    if os.path.exists(TEMP_DIR):
        for root, _, files in os.walk(TEMP_DIR):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    temp_size_bytes += os.path.getsize(fp)
                    temp_file_count += 1
                except OSError:
                    pass

    metrics["temp_render"] = {
        "size_mb": round(temp_size_bytes / (1024**2), 2),
        "file_count": temp_file_count
    }

    # Measure exports directory size
    export_size_bytes = 0
    export_file_count = 0
    if os.path.exists(EXPORTS_DIR):
        for root, _, files in os.walk(EXPORTS_DIR):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    export_size_bytes += os.path.getsize(fp)
                    export_file_count += 1
                except OSError:
                    pass

    metrics["exports"] = {
        "size_mb": round(export_size_bytes / (1024**2), 2),
        "file_count": export_file_count
    }

    # Retrieve thresholds from DB settings
    metrics["thresholds"] = get_storage_thresholds()
    
    # Assess safety
    min_headroom = metrics["thresholds"]["min_disk_headroom_gb"]
    current_free = metrics["project_drive"].get("free_gb", 0)
    metrics["is_safe_to_render"] = current_free >= min_headroom
    if not metrics["is_safe_to_render"]:
        metrics["warning"] = f"CRITICAL: Free disk space ({current_free} GB) is below safety limit ({min_headroom} GB). Rendering halted."
    else:
        metrics["warning"] = None

    return metrics

def get_storage_thresholds():
    """Fetches configurable storage limits from SQLite settings."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT key, value FROM system_settings WHERE key IN ('storage_limit_gb', 'min_disk_headroom_gb', 'auto_cleanup_temp')")
        rows = dict(cur.fetchall())
        conn.close()
        return {
            "storage_limit_gb": float(rows.get("storage_limit_gb", 2.0)),
            "min_disk_headroom_gb": float(rows.get("min_disk_headroom_gb", 5.0)),
            "auto_cleanup_temp": rows.get("auto_cleanup_temp", "true").lower() == "true"
        }
    except Exception:
        return {
            "storage_limit_gb": 2.0,
            "min_disk_headroom_gb": 5.0,
            "auto_cleanup_temp": True
        }

def cleanup_temporary_files(force_all=False):
    """
    Cleans up temp render files.
    If force_all is True, removes all files in temp_render.
    If force_all is False, removes files if temp folder exceeds storage_limit_gb.
    """
    ensure_directories()
    thresholds = get_storage_thresholds()
    limit_bytes = thresholds["storage_limit_gb"] * (1024**3)

    freed_bytes = 0
    deleted_files = 0

    if not os.path.exists(TEMP_DIR):
        return {"freed_mb": 0, "deleted_files": 0}

    # Get total size
    total_size = sum(
        os.path.getsize(os.path.join(root, f))
        for root, _, files in os.walk(TEMP_DIR)
        for f in files
        if os.path.exists(os.path.join(root, f))
    )

    if force_all or total_size > limit_bytes:
        for root, dirs, files in os.walk(TEMP_DIR, topdown=False):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    sz = os.path.getsize(fp)
                    os.remove(fp)
                    freed_bytes += sz
                    deleted_files += 1
                except OSError:
                    pass
            for d in dirs:
                dp = os.path.join(root, d)
                try:
                    os.rmdir(dp)
                except OSError:
                    pass

    return {
        "freed_mb": round(freed_bytes / (1024**2), 2),
        "deleted_files": deleted_files,
        "remaining_temp_mb": round((total_size - freed_bytes) / (1024**2), 2)
    }

def check_file_hash(file_path):
    """Calculates SHA-256 hash of a file for duplicate asset detection."""
    if not os.path.isfile(file_path):
        return None
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    import pprint
    pprint.pprint(get_disk_status())
