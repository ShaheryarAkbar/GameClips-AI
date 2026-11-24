import urllib.request
import urllib.parse
import os
import subprocess, json

url = "https://archive.org/download/grand-theft-auto-vi-trailer-1-4k-60fps_202405/Grand%20Theft%20Auto%20VI%20Trailer%201%20%284k%29.mp4"
dest = "assets/video/gta6_trailer_4k.mp4"

print(f"Downloading 4K GTA 6 footage ({url})...")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
    copied = 0
    while True:
        chunk = resp.read(1024 * 1024)
        if not chunk:
            break
        f.write(chunk)
        copied += len(chunk)
        if copied % (10 * 1024 * 1024) == 0:
            print(f"Downloaded {copied // (1024*1024)} MB...")

print(f"\nDownload finished! Size: {os.path.getsize(dest)} bytes")

# Check with ffprobe
cmd = ["ffprobe", "-v", "error", "-show_entries", "stream=width,height,codec_name,r_frame_rate:format=duration", "-of", "json", dest]
info = json.loads(subprocess.check_output(cmd))
print("Stream info:", info)
