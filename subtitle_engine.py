"""
GameClips AI - Subtitle Generation Engine
Produces synchronized SRT and ASS subtitles styled specifically for
vertical short-form video (YouTube Shorts & TikTok).
"""

import os

def format_timestamp_srt(seconds):
    """Converts seconds into SRT timestamp format: HH:MM:SS,mmm"""
    millis = int((seconds - int(seconds)) * 1000)
    total_sec = int(seconds)
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    secs = total_sec % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def format_timestamp_ass(seconds):
    """Converts seconds into ASS timestamp format: H:MM:SS.cc"""
    centis = int((seconds - int(seconds)) * 100)
    total_sec = int(seconds)
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    secs = total_sec % 60
    return f"{hours}:{minutes:02d}:{secs:02d}.{centis:02d}"

def generate_subtitles_for_scenes(scenes, output_srt_path, output_ass_path=None):
    """
    Builds synchronized SRT and ASS subtitle files from scene plans.
    """
    os.makedirs(os.path.dirname(output_srt_path), exist_ok=True)

    # 1. Generate standard SRT
    srt_blocks = []
    for idx, sc in enumerate(scenes):
        start_str = format_timestamp_srt(sc["start_time"])
        end_str = format_timestamp_srt(sc["end_time"])
        text = sc.get("subtitle_text") or sc.get("narration_text") or ""
        srt_blocks.append(f"{idx + 1}\n{start_str} --> {end_str}\n{text}\n")

    srt_content = "\n".join(srt_blocks)
    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

    # 2. Generate styled ASS if requested
    if output_ass_path:
        os.makedirs(os.path.dirname(output_ass_path), exist_ok=True)
        # ASS Header with high-contrast gaming subtitle styling
        ass_lines = [
            "[Script Info]",
            "Title: GameClips AI Vertical Subtitles",
            "ScriptType: v4.00+",
            "WrapStyle: 0",
            "PlayResX: 1080",
            "PlayResY: 1920",
            "",
            "[V4+ Styles]",
            "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
            # Style: Viral TikTok/Shorts Yellow font (&H0000FFFF), bold black outline (&H00000000), alignment 2 (bottom center), marginV 160 (lower-third center)
            "Style: Default,Segoe UI,46,&H0000FFFF,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,3.8,2,2,70,70,160,1",
            "",
            "[Events]",
            "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
        ]

        for sc in scenes:
            start_str = format_timestamp_ass(sc["start_time"])
            end_str = format_timestamp_ass(sc["end_time"])
            raw_text = sc.get("subtitle_text") or sc.get("narration_text") or ""
            # Wrap into 2 balanced lines if long
            words = raw_text.split()
            if len(words) > 7:
                mid = len(words) // 2
                wrapped_text = " ".join(words[:mid]) + "\\N" + " ".join(words[mid:])
            else:
                wrapped_text = raw_text
            ass_lines.append(f"Dialogue: 0,{start_str},{end_str},Default,,0,0,0,,{wrapped_text}")

        with open(output_ass_path, "w", encoding="utf-8") as f:
            f.write("\n".join(ass_lines))

    return {
        "srt_path": output_srt_path,
        "ass_path": output_ass_path
    }

if __name__ == "__main__":
    test_scenes = [
        {"start_time": 0.0, "end_time": 5.0, "subtitle_text": "Did you know this crazy GTA 6 secret?"},
        {"start_time": 5.0, "end_time": 15.0, "subtitle_text": "Rockstar confirmed Vice City is 2.5 times bigger than Los Santos."}
    ]
    res = generate_subtitles_for_scenes(test_scenes, "temp_render/test_subs.srt", "temp_render/test_subs.ass")
    print("Generated subtitles:", res)
