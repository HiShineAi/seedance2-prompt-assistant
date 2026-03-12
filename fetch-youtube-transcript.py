#!/usr/bin/env python3
"""
YouTube Transcript Fetcher with Proxy Support
Fetches transcript from a YouTube video URL using proxy
"""

import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Set proxy environment variables
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'

def extract_video_id(url):
    """Extract video ID from YouTube URL"""
    import re
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return url  # Return as-is if it's already a video ID

def main():
    if len(sys.argv) < 2:
        print('Usage: python fetch-youtube-transcript.py <youtube_url>')
        print('Example: python fetch-youtube-transcript.py https://www.youtube.com/watch?v=vCoGfisdS8Y')
        sys.exit(1)
    
    video_url = sys.argv[1]
    video_id = extract_video_id(video_url)
    
    print(f"\n=== YouTube Transcript Fetcher ===")
    print(f"Video URL: {video_url}")
    print(f"Video ID: {video_id}")
    print(f"Proxy: http://127.0.0.1:7890")
    print()
    
    try:
        print(f"Attempting to fetch transcript for video ID: {video_id}")
        print(f"Using proxy: http://127.0.0.1:7890")
        print()
        
        # Try with multiple languages
        languages = ['zh-Hans', 'zh-Hant', 'en', 'en-US', 'ja']
        
        # Try each language one by one
        transcript = None
        for lang in languages:
            try:
                print(f"Trying language: {lang}")
                # Correct API call for youtube-transcript-api
                from youtube_transcript_api import YouTubeTranscriptApi
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
                print(f"✅ Success! Found {len(transcript)} segments in {lang}")
                print()
                break
            except Exception as e:
                print(f"  Failed: {e}")
                continue
        
        if not transcript:
            # Try any available language
            print("Trying any available language...")
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                print(f"✅ Success! Found {len(transcript)} segments in available language")
                print()
            except Exception as e:
                print(f"  Failed: {e}")
                raise
        
        # Display first few segments
        print("First 10 segments:")
        for i, seg in enumerate(transcript[:10], 1):
            mins = seg['start'] // 60
            secs = int(seg['start'] % 60)
            time_str = f"{mins}:{secs:02d}"
            print(f"[{time_str}] {seg['text']}")
        
        print("\n--- Full Transcript ---")
        print()
        full_text = ' '.join([seg['text'] for seg in transcript])
        print(full_text)
        
        print("\n=== Summary ===")
        print(f"Total segments: {len(transcript)}")
        print(f"Transcript length: {len(full_text)} characters")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Possible solutions:")
        print("1. Make sure ClashX is running in global mode")
        print("2. Verify proxy port 7890 is correct")
        print("3. Check if YouTube is accessible through your proxy")
        print("4. Ensure the video has available subtitles")
        print("5. Try reinstalling youtube-transcript-api: pip install --upgrade youtube-transcript-api")

if __name__ == "__main__":
    main()