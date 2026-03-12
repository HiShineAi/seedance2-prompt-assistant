#!/usr/bin/env python3
"""
Fetch YouTube subtitles using pytube
"""

import os
import sys
from pytube import YouTube

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# 测试视频
if len(sys.argv) < 2:
    video_url = 'https://www.youtube.com/watch?v=vCoGfisdS8Y'
    print(f"Using default video: {video_url}")
else:
    video_url = sys.argv[1]

print(f"=== Fetching YouTube Subtitles ===")
print(f"Video: {video_url}")
print(f"Proxy: {os.environ['HTTPS_PROXY']}")
print()

try:
    # 初始化YouTube对象
    print("1. Initializing YouTube object...")
    yt = YouTube(video_url)
    print(f"   Title: {yt.title}")
    print(f"   Author: {yt.author}")
    print(f"   Length: {yt.length} seconds")
    print()
    
    # 获取所有可用的字幕
    print("2. Getting available captions...")
    captions = yt.captions
    
    if not captions:
        print("   ❌ No captions available for this video")
        sys.exit(1)
    
    print(f"   Available captions ({len(captions)}):")
    for caption in captions:
        print(f"   - {caption.code}: {caption.name}")
    print()
    
    # 尝试获取英文或中文字幕
    print("3. Selecting caption...")
    selected_caption = None
    preferred_languages = ['en', 'zh-Hans', 'zh-Hant', 'en-US']
    
    # 首先尝试首选语言
    for lang in preferred_languages:
        if lang in captions:
            selected_caption = captions[lang]
            print(f"   ✅ Found caption: {selected_caption.name}")
            break
    
    # 如果没有首选语言，使用第一个可用的
    if not selected_caption and captions:
        selected_caption = list(captions.values())[0]
        print(f"   ⚠️  Using first available caption: {selected_caption.name}")
    
    if selected_caption:
        # 获取字幕文本
        print("\n4. Fetching transcript...")
        transcript = selected_caption.generate_srt_captions()
        
        # 解析SRT格式
        lines = transcript.strip().split('\n')
        segments = []
        current_segment = {}
        
        for line in lines:
            line = line.strip()
            if line.isdigit():
                # 新的字幕段
                if current_segment:
                    segments.append(current_segment)
                current_segment = {'index': int(line)}
            elif ' --> ' in line:
                # 时间范围
                current_segment['time'] = line
            elif line:
                # 字幕文本
                current_segment['text'] = current_segment.get('text', '') + line + ' '
        
        if current_segment:
            segments.append(current_segment)
        
        print(f"   ✅ Successfully fetched {len(segments)} segments")
        print()
        
        # 显示前10个字幕段
        print("5. First 10 segments:")
        for seg in segments[:10]:
            print(f"   [{seg['time']}] {seg['text'].strip()}")
        
        # 显示完整字幕
        print("\n6. Full transcript:")
        print('=' * 50)
        full_text = ' '.join([seg['text'].strip() for seg in segments])
        print(full_text)
        print('=' * 50)
        
        print(f"\n7. Summary:")
        print(f"   Total segments: {len(segments)}")
        print(f"   Transcript length: {len(full_text)} characters")
        print(f"   Video: {yt.title}")
        print(f"   Caption language: {selected_caption.name}")
        
    else:
        print("   ❌ No captions available")
        
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