---
name: video-downloader
description: Download videos from YouTube and other platforms using yt-dlp. Use this skill when users request to download videos from URLs (YouTube, Vimeo, TikTok, Twitter, Instagram, etc.) or ask for video/audio extraction.
---

# Video Downloader

This skill provides functionality to download videos and audio from various online platforms using yt-dlp.

## Supported Platforms

yt-dlp supports 1000+ websites including:
- YouTube (all formats)
- Vimeo
- TikTok
- Twitter/X
- Instagram
- Facebook
- Twitch
- Dailymotion
- SoundCloud
- Bilibili
- And many more...

## Basic Workflow

### Download Video (Best Quality)

When a user asks to download a video:

1. **Ask for preferences** (optional):
   - Output format (MP4, MKV, etc.)
   - Resolution (1080p, 720p, etc.)
   - Output directory

2. **Use the download script**:
   ```bash
   python3 .claude/skills/video-downloader/scripts/download.py <URL>
   ```

3. **Report results** to the user:
   - Download status
   - File location
   - File size
   - Duration

### Download Audio Only

When a user wants audio only:

```bash
python3 .claude/skills/video-downloader/scripts/download.py <URL> --audio-only
```

### Download with Custom Quality

To download with specific format/resolution:

```bash
python3 .claude/skills/video-downloader/scripts/download.py <URL> --format <format_string>
```

Common format strings:
- `best` - Best quality
- `worst` - Worst quality
- `bestvideo+bestaudio` - Best video and audio combined
- `137+140` - 1080p video + m4a audio
- `22` - 720p MP4
- `18` - 360p MP4

### Download Playlist

To download an entire playlist:

```bash
python3 .claude/skills/video-downloader/scripts/download.py <PLAYLIST_URL> --playlist
```

### Extract Subtitles

To download subtitles:

```bash
python3 .claude/skills/video-downloader/scripts/download.py <URL> --subs
```

### Get Video Info Only

To get information without downloading:

```bash
python3 .claude/skills/video-downloader/scripts/download.py <URL> --info
```

## Available Options

| Option | Description |
|--------|-------------|
| `--audio-only` | Download audio only (MP3) |
| `--format <fmt>` | Specify video format |
| `--playlist` | Download entire playlist |
| `--subs` | Download subtitles |
| `--info` | Get video info only |
| `--output <path>` | Custom output directory |
| `--embed-subs` | Embed subtitles in video |
| `--thumbnail` | Download thumbnail |

## Example Usage

```
User: "Download this video: https://www.youtube.com/watch?v=dQw4w9WgXcQ"

Claude: Downloading video...
✓ Downloaded to: ~/Downloads/Rick Astley - Never Gonna Give You Up [dQw4w9WgXcQ].mp4
  Size: 8.2 MB
  Duration: 3:33
```

```
User: "Get just the audio from this TikTok: https://www.tiktok.com/@user/video/123"

Claude: Downloading audio only...
✓ Downloaded to: ~/Downloads/video_audio.mp3
  Size: 2.1 MB
  Duration: 0:45
```

```
User: "What's the resolution of this video? https://www.youtube.com/watch?v=abc123"

Claude: Video Information:
  Title: Example Video
  Duration: 10:24
  Views: 1,234,567
  Available formats:
    - 1080p (MP4)
    - 720p (MP4)
    - 480p (MP4)
```

## Notes

- Downloaded files are saved to `~/Downloads/` by default
- Videos are downloaded in MP4 format unless specified
- For long videos, the download may take time
- Some sites may require cookies or login for certain content

## Troubleshooting

If download fails:
1. Check if URL is valid
2. Ensure internet connection is stable
3. Some content may be geo-restricted
4. Try using `--format worst` for better compatibility
