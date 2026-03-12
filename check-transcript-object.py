#!/usr/bin/env python3
"""
Check FetchedTranscript object structure
"""

import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# 测试视频（已知有字幕）
video_url = 'https://www.youtube.com/watch?v=rfscVS0vtbw'

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
    return url

video_id = extract_video_id(video_url)

print(f"=== Checking FetchedTranscript Object ===")
print(f"Video ID: {video_id}")
print()

try:
    # 创建API实例
    api = YouTubeTranscriptApi()
    
    # 获取字幕
    transcript = api.fetch(video_id, languages=['en'])
    
    print("1. FetchedTranscript object created successfully")
    print(f"   Type: {type(transcript)}")
    print()
    
    # 检查对象属性
    print("2. Object attributes:")
    for attr in dir(transcript):
        if not attr.startswith('_'):
            print(f"   - {attr}")
    print()
    
    # 检查对象方法
    print("3. Object methods:")
    for attr in dir(transcript):
        if not attr.startswith('_') and callable(getattr(transcript, attr)):
            print(f"   - {attr}")
    print()
    
    # 尝试获取字幕内容的不同方法
    print("4. Trying different ways to get transcript content:")
    
    # 方法1: 直接打印对象
    print("   Method 1: Direct print")
    print(f"   Type: {type(transcript)}")
    print()
    
    # 方法2: 检查是否可迭代
    print("   Method 2: Checking if iterable")
    try:
        print(f"   Is iterable: True")
        # 尝试迭代
        print("   First 3 items:")
        for i, item in enumerate(transcript[:3]):
            print(f"     {i+1}: {type(item)} - {item}")
    except Exception as e:
        print(f"   Is iterable: False")
    print()
    
    # 方法3: 检查是否有text属性
    print("   Method 3: Checking text attribute")
    if hasattr(transcript, 'text'):
        text = transcript.text
        print(f"   Has text attribute: True")
        print(f"   Text length: {len(text)} characters")
        print(f"   First 200 chars: {text[:200]}...")
    else:
        print(f"   Has text attribute: False")
    print()
    
    # 方法4: 检查是否有to_dict方法
    print("   Method 4: Checking to_dict method")
    if hasattr(transcript, 'to_dict'):
        transcript_dict = transcript.to_dict()
        print(f"   Has to_dict method: True")
        print(f"   Dict keys: {list(transcript_dict.keys())}")
        if 'segments' in transcript_dict:
            print(f"   Segments count: {len(transcript_dict['segments'])}")
            print(f"   First segment: {transcript_dict['segments'][0]}")
    else:
        print(f"   Has to_dict method: False")
    print()
    
    # 方法5: 检查__dict__属性
    print("   Method 5: Checking __dict__")
    print(f"   __dict__ keys: {list(transcript.__dict__.keys())}")
    if '_segments' in transcript.__dict__:
        print(f"   Found _segments attribute")
        print(f"   Segments count: {len(transcript.__dict__['_segments'])}")
        print(f"   First segment: {transcript.__dict__['_segments'][0]}")
    print()
    
    print("=== Check complete ===")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()