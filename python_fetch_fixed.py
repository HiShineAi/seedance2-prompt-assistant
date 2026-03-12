#!/usr/bin/env python3
"""
YouTube Transcript Fetcher with Proxy Support
"""

import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Set proxy
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

# Get video ID from command line or use default
if len(sys.argv) > 1:
    video_id = sys.argv[1]
else:
    video_id = 'HA6XxtGNOm0'

print(f"Attempting to fetch transcript for video ID: {video_id}")
print(f"Using proxy: http://127.0.0.1:7890\n")

try:
    # Use correct API call - create instance first
    api = YouTubeTranscriptApi()
    
    # Fetch transcript with multiple language options
    transcript = api.fetch(video_id, languages=['en', 'zh-Hans', 'zh-Hant'])

    print(f"✅ Success! Found {len(transcript.snippets)} segments")
    print(f"Language: {transcript.language} ({transcript.language_code})")
    print(f"Auto-generated: {transcript.is_generated}\n")

    print("First 10 segments:")
    for i, snippet in enumerate(transcript.snippets[:10], 1):
        mins = int(snippet.start // 60)
        secs = int(snippet.start % 60)
        time_str = f"{mins}:{secs:02d}"
        print(f"[{time_str}] {snippet.text}")

    print("\n--- Full Transcript ---\n")
    full_text = ' '.join([snippet.text for snippet in transcript.snippets])
    print(full_text)

    print("\n=== Summary ===")
    print(f"Total segments: {len(transcript.snippets)}")
    print(f"Transcript length: {len(full_text)} characters")

except Exception as e:
    print(f"❌ Error: {e}")
    print("\nPossible solutions:")
    print("1. Check if ClashX is in global mode")
    print("2. Verify port 7890 is correct HTTP proxy")
    print("3. Try changing DNS to 8.8.8.8")
    import traceback
    traceback.print_exc()