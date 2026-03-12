#!/usr/bin/env python3
"""
Fetch YouTube transcript using correct API for youtube-transcript-api library
"""

import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# 测试视频
if len(sys.argv) < 2:
    video_url = 'https://www.youtube.com/watch?v=vCoGfisdS8Y'
    print(f"Using default video: {video_url}")
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
    print("1. Using YouTubeTranscriptApi.fetch() method...")
    print(f"   Fetching transcript for video ID: {video_id}")
    
    # 使用正确的API方法
    transcript_list = YouTubeTranscriptApi.fetch(video_id)
    
    print(f"   ✅ Successfully fetched transcript list")
    print()
    
    # 显示可用的字幕
    print("2. Available transcripts:")
    for transcript in transcript_list:
        print(f"   - {transcript.language_code}: {transcript.language}")
    print()
    
    # 选择合适的字幕
    print("3. Selecting transcript...")
    selected_transcript = None
    
    # 尝试获取英文或中文字幕
    preferred_languages = ['en', 'zh-Hans', 'zh-Hant']
    
    for lang in preferred_languages:
        for transcript in transcript_list:
            if transcript.language_code == lang:
                selected_transcript = transcript
                print(f"   ✅ Found transcript: {transcript.language} ({transcript.language_code})")
                break
        if selected_transcript:
            break
    
    # 如果没有首选语言，使用第一个可用的
    if not selected_transcript and transcript_list:
        selected_transcript = transcript_list[0]
        print(f"   ⚠️  Using first available transcript: {selected_transcript.language} ({selected_transcript.language_code})")
    
    if selected_transcript:
        # 获取字幕文本
        print("\n4. Getting transcript text...")
        segments = selected_transcript.segments
        
        print(f"   ✅ Successfully fetched {len(segments)} segments")
        print()
        
        # 显示前10个字幕段
        print("5. First 10 segments:")
        for i, seg in enumerate(segments[:10], 1):
            start = seg['start']
            duration = seg['duration']
            text = seg['text']
            
            mins = int(start // 60)
            secs = int(start % 60)
            time_str = f"{mins}:{secs:02d}"
            
            print(f"   [{time_str}] {text}")
        
        # 显示完整字幕
        print("\n6. Full transcript:")
        print('=' * 50)
        full_text = ' '.join([seg['text'] for seg in segments])
        print(full_text)
        print('=' * 50)
        
        print(f"\n7. Summary:")
        print(f"   Total segments: {len(segments)}")
        print(f"   Transcript length: {len(full_text)} characters")
        print(f"   Language: {selected_transcript.language} ({selected_transcript.language_code})")
    else:
        print("   ❌ No transcripts available")
        
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