
import subprocess
import sys
import os
from datetime import datetime

DOWNLOAD_DIR = "downloads"

def download_video(url):
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    output_template = os.path.join(
        DOWNLOAD_DIR,
        "%(title)s_%(id)s.%(ext)s"
    )

    command = [
        "yt-dlp",
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", output_template,
        "--no-playlist",
        url
    ]

    print("\n📥 Starting download...")
    print("🔗 URL:", url)

    try:
        subprocess.run(command, check=True)
        print("\n✅ Download completed successfully!")
    except subprocess.CalledProcessError:
        print("\n❌ Download failed. Check the URL or platform restrictions.")

def main():
    print("===================================")
    print("🎥 Universal Video Downloader")
    print("===================================")
    print("Supported: YouTube | Instagram | Twitter/X | Facebook\n")

    while True:
        url = input("🔗 Paste video URL (or type 'exit'): ").strip()

        if url.lower() == "exit":
            print("\n👋 Exiting program.")
            break

        if not url.startswith("http"):
            print("⚠️ Invalid URL. Try again.\n")
            continue

        download_video(url)
        print("\n-----------------------------------\n")

if __name__ == "__main__":
    main()
