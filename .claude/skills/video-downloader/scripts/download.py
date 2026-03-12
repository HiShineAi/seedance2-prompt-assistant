#!/usr/bin/env python3
"""
Video Downloader Script using yt-dlp

Usage:
    python3 download.py <URL> [options]

Options:
    --audio-only      Download audio only (MP3)
    --format <fmt>    Specify video format (best, worst, 137+140, 22, 18, etc.)
    --playlist        Download entire playlist
    --subs            Download subtitles
    --info            Get video info only (no download)
    --output <path>   Custom output directory
    --embed-subs      Embed subtitles in video
    --thumbnail       Download thumbnail
"""

import sys
import argparse
import os
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp not installed. Run: pip3 install yt-dlp")
    sys.exit(1)


def get_video_info(url):
    """Get video information without downloading."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None


def format_video_info(info):
    """Format video information for display."""
    if not info:
        return "No information available."

    lines = []
    lines.append(f"Title: {info.get('title', 'N/A')}")
    lines.append(f"Duration: {info.get('duration_string', 'N/A')}")
    lines.append(f"Views: {info.get('view_count', 'N/A'):,}")
    lines.append(f"Uploader: {info.get('uploader', 'N/A')}")
    lines.append(f"Upload Date: {info.get('upload_date', 'N/A')}")

    # Format information
    if 'formats' in info:
        lines.append("\nAvailable Formats:")
        seen = set()
        for fmt in info.get('formats', []):
            ext = fmt.get('ext', '')
            height = fmt.get('height', 'N/A')
            fps = fmt.get('fps', 'N/A')
            key = f"{ext}-{height}-{fps}"
            if key not in seen and fmt.get('vcodec') != 'none':
                lines.append(f"  - {ext} {height}p @ {fps}fps")
                seen.add(key)

    return '\n'.join(lines)


def download_video(url, args):
    """Download video or audio."""
    # Default output directory
    output_dir = Path(args.output or Path.home() / "Downloads")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build output template
    output_template = str(output_dir / "%(title)s [%(id)s].%(ext)s")

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': output_template,
        'quiet': False,
        'no_warnings': False,
        'progress_hooks': [progress_hook],
    }

    # Audio only
    if args.audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

    # Custom format
    elif args.format:
        ydl_opts['format'] = args.format

    # Default: best video + audio
    else:
        ydl_opts['format'] = 'bestvideo+bestaudio/best'

    # Subtitles
    if args.subs:
        ydl_opts.update({
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en', 'zh-Hans', 'zh-Hant'],
        })

    # Embed subtitles
    if args.embed_subs:
        ydl_opts['subtitleslangs'] = ['en', 'zh-Hans', 'zh-Hant']
        ydl_opts['writessubtitles'] = True
        ydl_opts['writeautomaticsub'] = True

    # Thumbnail
    if args.thumbnail:
        ydl_opts['writethumbnail'] = True

    # Playlist
    if args.playlist:
        ydl_opts['ignoreerrors'] = True

    # Download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            return True
        except Exception as e:
            print(f"\nError: {e}")
            return False


def progress_hook(d):
    """Display download progress."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        print("\rDownload complete! Processing...", end='', flush=True)


def main():
    parser = argparse.ArgumentParser(description='Download videos using yt-dlp')
    parser.add_argument('url', help='Video URL')
    parser.add_argument('--audio-only', action='store_true', help='Download audio only')
    parser.add_argument('--format', '-f', help='Video format (e.g., best, 22, 137+140)')
    parser.add_argument('--playlist', action='store_true', help='Download playlist')
    parser.add_argument('--subs', action='store_true', help='Download subtitles')
    parser.add_argument('--info', action='store_true', help='Get video info only')
    parser.add_argument('--output', '-o', help='Output directory')
    parser.add_argument('--embed-subs', action='store_true', help='Embed subtitles')
    parser.add_argument('--thumbnail', action='store_true', help='Download thumbnail')

    args = parser.parse_args()

    # Info only mode
    if args.info:
        print("Fetching video information...")
        info = get_video_info(args.url)
        print(format_video_info(info))
        return

    # Download mode
    print(f"Downloading from: {args.url}")
    if args.audio_only:
        print("Mode: Audio only (MP3)")
    elif args.format:
        print(f"Mode: Custom format ({args.format})")
    else:
        print("Mode: Best quality video")

    success = download_video(args.url, args)

    if success:
        print(f"\n✓ Download complete!")
        output_dir = args.output or str(Path.home() / "Downloads")
        print(f"  Output: {output_dir}")
    else:
        print(f"\n✗ Download failed!")


if __name__ == '__main__':
    main()
