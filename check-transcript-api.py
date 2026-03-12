#!/usr/bin/env python3
"""
Check youtube-transcript-api actual API structure
"""

import os
import sys

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

print("=== Checking youtube-transcript-api ===")
print()

# 尝试不同的导入方式
try:
    print("1. Trying import youtube_transcript_api...")
    import youtube_transcript_api
    print(f"   Module imported successfully")
    print(f"   Module contents: {[attr for attr in dir(youtube_transcript_api) if not attr.startswith('_')]}")
    print()
    
except Exception as e:
    print(f"   Error: {e}")
    print()

try:
    print("2. Trying from youtube_transcript_api import *...")
    from youtube_transcript_api import *
    print(f"   Imported successfully")
    print(f"   Available attributes: {[attr for attr in dir() if not attr.startswith('_')]}")
    print()
    
except Exception as e:
    print(f"   Error: {e}")
    print()

try:
    print("3. Trying specific imports...")
    from youtube_transcript_api._api import YouTubeTranscriptApi
    print(f"   Imported YouTubeTranscriptApi successfully")
    print(f"   API attributes: {[attr for attr in dir(YouTubeTranscriptApi) if not attr.startswith('_')]}")
    print()
    
    # 检查是否有get_transcript方法
    if hasattr(YouTubeTranscriptApi, 'get_transcript'):
        print("   ✅ YouTubeTranscriptApi has get_transcript method")
    else:
        print("   ❌ YouTubeTranscriptApi has NO get_transcript method")
        print("   Available methods:")
        for attr in dir(YouTubeTranscriptApi):
            if not attr.startswith('_') and callable(getattr(YouTubeTranscriptApi, attr)):
                print(f"     - {attr}")
    
    print()
    
except Exception as e:
    print(f"   Error: {e}")
    import traceback
    traceback.print_exc()
    print()

try:
    print("4. Trying direct import from youtube_transcript_api...")
    from youtube_transcript_api import YouTubeTranscriptApi
    print(f"   Imported successfully")
    print(f"   API attributes: {[attr for attr in dir(YouTubeTranscriptApi) if not attr.startswith('_')]}")
    print()
    
except Exception as e:
    print(f"   Error: {e}")
    print()

print("=== Check complete ===")