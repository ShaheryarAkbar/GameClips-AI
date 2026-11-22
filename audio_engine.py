"""
GameClips AI - Audio Engine
Generates offline speech narration using Windows Native SAPI,
measures exact durations, and supports silent mode fallbacks.
"""

import os
import subprocess
import wave
from datetime import datetime
from database import get_connection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp_render")
SYNTHESIZE_SCRIPT = os.path.join(BASE_DIR, "synthesize.ps1")

def get_audio_duration_wave(wav_path):
    """Measures audio duration in seconds using Python's built-in wave module."""
    try:
        with wave.open(wav_path, "r") as w:
            frames = w.getnframes()
            rate = w.getframerate()
            return round(frames / float(rate), 2)
    except Exception:
        # Fallback to ffprobe
        try:
            cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", wav_path]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return round(float(res.stdout.strip()), 2)
        except Exception:
            return 0.0

def create_silent_audio(output_wav, duration_seconds=10.0, sample_rate=22050):
    """Creates a silent WAV file for silent mode generation."""
    os.makedirs(os.path.dirname(output_wav), exist_ok=True)
    num_frames = int(duration_seconds * sample_rate)
    with wave.open(output_wav, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(b"\x00" * (num_frames * 2))
    return duration_seconds

def generate_offline_speech(text, voice_name="Microsoft David Desktop", project_id="temp", output_wav=None):
    """
    Synthesizes narration text using Windows Native System.Speech.
    Returns audio metadata and duration.
    """
    audio_dir = os.path.join(TEMP_DIR, "audio")
    os.makedirs(audio_dir, exist_ok=True)

    if not output_wav:
        output_wav = os.path.join(audio_dir, f"{project_id}_voice.wav")

    # Silent mode check
    if voice_name == "SILENT" or not text.strip():
        duration = create_silent_audio(output_wav, duration_seconds=15.0)
        return {
            "success": True,
            "audio_path": output_wav,
            "duration": duration,
            "voice_name": "SILENT",
            "is_silent": True
        }

    # Execute PowerShell SAPI synthesis
    cmd = [
        "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
        "-File", SYNTHESIZE_SCRIPT,
        "-Text", text,
        "-Voice", voice_name,
        "-OutputFile", output_wav
    ]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        if result.returncode != 0 or not os.path.isfile(output_wav):
            # Fallback to silent mode on any system error
            duration = create_silent_audio(output_wav, duration_seconds=20.0)
            return {
                "success": True,
                "audio_path": output_wav,
                "duration": duration,
                "voice_name": "FALLBACK_SILENT",
                "is_silent": True
            }

        duration = get_audio_duration_wave(output_wav)

        # Record in audio_assets table
        conn = get_connection()
        try:
            cur = conn.cursor()
            # Verify foreign key existence for project_id
            actual_proj_id = None
            if project_id:
                cur.execute("SELECT id FROM video_projects WHERE id = ?", (project_id,))
                p_row = cur.fetchone()
                if p_row:
                    actual_proj_id = p_row["id"]

            audio_id = f"aud-{int(datetime.now().timestamp())}"
            cur.execute("""
            INSERT INTO audio_assets (
                id, project_id, audio_type, voice_name, file_path,
                duration_seconds, sample_rate, license_status, created_at
            ) VALUES (?, ?, 'TTS', ?, ?, ?, 22050, 'SYSTEM_OFFLINE_FREE', ?)
            """, (audio_id, actual_proj_id, voice_name, output_wav, duration, datetime.now().isoformat()))
            conn.commit()
        finally:
            conn.close()

        return {
            "success": True,
            "audio_path": output_wav,
            "duration": duration,
            "voice_name": voice_name,
            "is_silent": False
        }
    except Exception as e:
        duration = create_silent_audio(output_wav, duration_seconds=20.0)
        return {
            "success": True,
            "audio_path": output_wav,
            "duration": duration,
            "voice_name": "ERROR_SILENT",
            "is_silent": True,
            "error": str(e)
        }

if __name__ == "__main__":
    res = generate_offline_speech("Testing GameClips AI speech engine for GTA 6 video automation.", "Microsoft David Desktop", "test_proj")
    print("Result:", res)
