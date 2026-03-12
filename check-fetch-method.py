#!/usr/bin/env python3
"""
Check YouTubeTranscriptApi.fetch method signature
"""

import inspect
from youtube_transcript_api import YouTubeTranscriptApi

print("=== Checking YouTubeTranscriptApi.fetch Method ===")
print()

# 检查fetch方法的签名
print("1. Checking fetch method signature...")
try:
    sig = inspect.signature(YouTubeTranscriptApi.fetch)
    print(f"   Signature: {sig}")
    print(f"   Parameters: {list(sig.parameters.keys())}")
    print()
except Exception as e:
    print(f"   Error: {e}")
    print()

# 检查list方法的签名
print("2. Checking list method signature...")
try:
    sig = inspect.signature(YouTubeTranscriptApi.list)
    print(f"   Signature: {sig}")
    print(f"   Parameters: {list(sig.parameters.keys())}")
    print()
except Exception as e:
    print(f"   Error: {e}")
    print()

# 检查是否需要实例化
print("3. Checking if YouTubeTranscriptApi is a class...")
try:
    print(f"   Is class: {inspect.isclass(YouTubeTranscriptApi)}")
    
    # 尝试创建实例
    print("4. Trying to create instance...")
    api = YouTubeTranscriptApi()
    print(f"   ✅ Instance created successfully")
    
    # 检查实例方法
    print("5. Checking instance methods...")
    print(f"   Instance attributes: {[attr for attr in dir(api) if not attr.startswith('_')]}")
    print()
    
    # 检查实例的fetch方法
    if hasattr(api, 'fetch'):
        print("6. Checking instance fetch method...")
        sig = inspect.signature(api.fetch)
        print(f"   Signature: {sig}")
        print(f"   Parameters: {list(sig.parameters.keys())}")
    
    print()
    
except Exception as e:
    print(f"   Error: {e}")
    import traceback
    traceback.print_exc()
    print()

print("=== Check complete ===")