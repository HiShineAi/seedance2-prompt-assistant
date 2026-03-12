#!/usr/bin/env python3
"""
Fetch YouTube transcript using correct instance-based API
"""

import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# 测试视频
if len(sys.argv) < 2:
    video_url = 'https://www.youtube.com/watch?v=rfscVS0vtbw'  # 已知有字幕的视频
    print(f"Using default video with subtitles: {video_url}")
else:
    video_url = sys.argv[1]

# 提取视频ID
def extract_video_id(url):
    import re
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return url  # Return as-is if it's already a video ID

video_id = extract_video_id(video_url)

print(f"=== Fetching YouTube Transcript ===")
print(f"Video URL: {video_url}")
print(f"Video ID: {video_id}")
print(f"Proxy: {os.environ['HTTPS_PROXY']}")
print()

try:
    print("1. Creating YouTubeTranscriptApi instance...")
    api = YouTubeTranscriptApi()
    print(f"   ✅ Instance created successfully")
    print()
    
    print("2. Fetching transcript...")
    print(f"   Fetching transcript for video ID: {video_id}")
    
    # 使用正确的实例方法调用
    transcript = api.fetch(video_id, languages=['en', 'zh-Hans', 'zh-Hant'])
    
    print(f"   ✅ Successfully fetched transcript")
    print(f"   Language: {transcript.language} ({transcript.language_code})")
    print()
    
    # 获取字幕段
    print("3. Processing transcript segments...")
    segments = transcript.segments
    
    print(f"   ✅ Found {len(segments)} segments")
    print()
    
    # 显示前10个字幕段
    print("4. First 10 segments:")
    for i, seg in enumerate(segments[:10], 1):
        start = seg['start']
        text = seg['text']
        
        mins = int(start // 60)
        secs = int(start % 60)
        time_str = f"{mins}:{secs:02d}"
        
        print(f"   [{time_str}] {text}")
    
    # 显示完整字幕
    print("\n5. Full transcript:")
    print('=' * 50)
    full_text = ' '.join([seg['text'] for seg in segments])
    print(full_text)
    print('=' * 50)
    
    print(f"\n6. Summary:")
    print(f"   Total segments: {len(segments)}")
    print(f"   Transcript length: {len(full_text)} characters")
    print(f"   Language: {transcript.language} ({transcript.language_code})")
    print(f"   Video ID: {video_id}")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print()
    print("Possible solutions:")
    print("1. Make sure ClashX is running in global mode")
    print("2. Check if the video has available subtitles")
    print("3. Try a different video URL")
    print("4. Verify your proxy configuration")
    import traceback
    traceback.print_exc()