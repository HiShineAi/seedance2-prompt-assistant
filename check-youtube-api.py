#!/usr/bin/env python3
"""
Check YouTube Transcript API structure
"""

import sys
import os

# Set proxy
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

try:
    print("Importing youtube_transcript_api...")
    import youtube_transcript_api
    print(f"Version: {youtube_transcript_api.__version__}")
    print()
    
    print("Checking module structure...")
    print(f"Module attributes: {[attr for attr in dir(youtube_transcript_api) if not attr.startswith('_')]}")
    print()
    
    # Try different import methods
    print("Trying direct import...")
    from youtube_transcript_api import YouTubeTranscriptApi
    print(f"YouTubeTranscriptApi attributes: {[attr for attr in dir(YouTubeTranscriptApi) if not attr.startswith('_')]}")
    print()
    
    # Check if get_transcript exists
    print(f"Has get_transcript: {'get_transcript' in dir(YouTubeTranscriptApi)}")
    print()
    
    # Try alternative import
    print("Trying alternative import...")
    import youtube_transcript_api._api
    print(f"_api attributes: {[attr for attr in dir(youtube_transcript_api._api) if not attr.startswith('_')]}")
    print()
    
    # Try to create instance
    print("Trying to create instance...")
    try:
        api = YouTubeTranscriptApi()
        print(f"Instance created successfully")
        print(f"Instance attributes: {[attr for attr in dir(api) if not attr.startswith('_')]}")
    except Exception as e:
        print(f"Failed to create instance: {e}")
    
    print("\n=== Summary ===")
    print("The library seems to be installed but the API structure might be different.")
    print("Let me try a different approach.")
    
    # Try a different method using requests directly
    print("\nTrying direct HTTP request with proxy...")
    import requests
    
    video_id = "vCoGfisdS8Y"
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    
    try:
        response = requests.get(url, proxies=proxies, timeout=30)
        print(f"YouTube access: {'Success' if response.status_code == 200 else 'Failed'}")
        print(f"Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to access YouTube: {e}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()