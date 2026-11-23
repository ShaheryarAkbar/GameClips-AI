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

def synthesize_neural_edge_tts(text, voice_name="en-US-ChristopherNeural", output_wav=None):
    """
    Generates studio-grade cinematic narration using neural edge-tts.
    Zero paid API keys, zero cloud billing. Produces professional YouTube/TikTok voiceover.
    """
    import asyncio
    try:
        import edge_tts
        temp_mp3 = output_wav.replace(".wav", "_temp.mp3")
        async def _run():
            communicate = edge_tts.Communicate(text, voice_name, rate="+4%")
            await communicate.save(temp_mp3)
        asyncio.run(_run())
        if os.path.isfile(temp_mp3):
            # Convert to standard 44.1kHz WAV
            subprocess.run([
                "ffmpeg", "-y", "-i", temp_mp3,
                "-ar", "44100", "-ac", "2",
                output_wav
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            if os.path.isfile(temp_mp3):
                try: os.remove(temp_mp3)
                except Exception: pass
            return True
    except Exception as e:
        print("[WARN] Neural TTS error, falling back to SAPI:", e)
    return False

def generate_offline_speech(text, voice_name="en-US-ChristopherNeural", project_id="temp", output_wav=None):
    """
    Synthesizes narration text using high-quality Neural TTS (or Windows Native SAPI fallback).
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

    # 1. Attempt High-Fidelity Studio Neural Narration (YouTube/TikTok Viral Gaming Style)
    neural_voices = ["en-US-ChristopherNeural", "en-US-GuyNeural", "en-US-EricNeural", "en-US-BrianNeural"]
    selected_neural = voice_name if voice_name in neural_voices or voice_name.startswith("en-") else "en-US-ChristopherNeural"
    neural_success = synthesize_neural_edge_tts(text, selected_neural, output_wav)

    if not neural_success or not os.path.isfile(output_wav):
        # 2. Seamless Fallback to Windows Native SAPI
        sapi_voice = "Microsoft David Desktop"
        if "zira" in voice_name.lower():
            sapi_voice = "Microsoft Zira Desktop"

        cmd = [
            "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
            "-File", SYNTHESIZE_SCRIPT,
            "-Text", text,
            "-Voice", sapi_voice,
            "-OutputFile", output_wav
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        if result.returncode != 0 or not os.path.isfile(output_wav):
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
        ) VALUES (?, ?, 'TTS', ?, ?, ?, 44100, 'SYSTEM_OFFLINE_FREE', ?)
        """, (audio_id, actual_proj_id, selected_neural if neural_success else voice_name, output_wav, duration, datetime.now().isoformat()))
        conn.commit()
    finally:
        conn.close()

    return {
        "success": True,
        "audio_path": output_wav,
        "duration": duration,
        "voice_name": selected_neural if neural_success else voice_name,
        "is_silent": False,
        "neural": neural_success
    }

if __name__ == "__main__":
    res = generate_offline_speech("Testing GameClips AI speech engine for GTA 6 video automation.", "Microsoft David Desktop", "test_proj")
    print("Result:", res)
