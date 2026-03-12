#!/usr/bin/env python3
"""
Simple YouTube Transcript Fetcher
Uses direct HTTP requests with proxy to fetch YouTube transcripts
"""

import sys
import os
import re
import json
import requests

# Use system default proxy (when ClashX is in global mode)
proxies = None

# Don't set environment variables when using global mode
# Let system handle proxy through ClashX global mode

def extract_video_id(url):
    """Extract video ID from YouTube URL"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return url  # Return as-is if it's already a video ID

def fetch_transcript(video_id):
    """Fetch transcript using direct HTTP requests"""
    print(f"Fetching transcript for video ID: {video_id}")
    print(f"Using proxy: {proxies['https'] if proxies else 'System default (ClashX global mode)'}")
    
    # Step 1: Get video page to find transcript URL
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    try:
        print("\n1. Fetching video page...")
        # Only use proxies if explicitly set
        response = requests.get(video_url, proxies=proxies, timeout=30)
        response.raise_for_status()
        print(f"   Status: {response.status_code}")
        
        # Step 2: Extract transcript URL from page
        print("\n2. Extracting transcript URL...")
        
        # Look for transcript API endpoint
        transcript_match = re.search(r'"captions"\s*:\s*\{[^}]*"playerCaptionsTracklistRenderer"\s*:\s*\{([^}]*)\}', 
                                   response.text, re.DOTALL)
        
        if not transcript_match:
            print("   ❌ No transcript found on page")
            return None
        
        captions_data = transcript_match.group(1)
        
        # Extract base URL for transcripts
        base_url_match = re.search(r'"baseUrl"\s*:\s*"([^"]+)"', captions_data)
        if not base_url_match:
            print("   ❌ No transcript base URL found")
            return None
        
        base_url = base_url_match.group(1).replace('\\u0026', '&')
        print(f"   Found transcript base URL")
        
        # Step 3: Fetch transcript data
        print("\n3. Fetching transcript data...")
        # Only use proxies if explicitly set
        transcript_response = requests.get(base_url, proxies=proxies, timeout=30)
        transcript_response.raise_for_status()
        print(f"   Status: {transcript_response.status_code}")
        
        # Step 4: Parse transcript data
        print("\n4. Parsing transcript...")
        transcript_data = transcript_response.text
        
        # Print first few lines of transcript data for debugging
        print("   First 20 lines of transcript data:")
        for i, line in enumerate(transcript_data.split('\n')[:20], 1):
            print(f"      {i}: {line}")
        
        # Extract text segments
        segments = []
        
        # Try different parsing methods
        # Method 1: Simple XML parsing
        print("\n   Trying XML parsing...")
        for line in transcript_data.split('\n'):
            if '<text' in line:
                # Extract start time and duration
                start_match = re.search(r'start="([^"]+)"', line)
                dur_match = re.search(r'dur="([^"]+)"', line)
                
                if start_match:
                    start = float(start_match.group(1))
                    dur = float(dur_match.group(1)) if dur_match else 0
                    
                    # Extract text content
                    text_match = re.search(r'>([^<]+)<\/text>', line)
                    if text_match:
                        text = text_match.group(1).strip()
                        segments.append({
                            'start': start,
                            'duration': dur,
                            'text': text
                        })
        
        if segments:
            print(f"   Found {len(segments)} segments using XML parsing")
            return segments
        
        # Method 2: Look for JSON format
        print("\n   Trying JSON parsing...")
        try:
            # Check if transcript data is JSON
            if transcript_data.strip().startswith('{'):
                data = json.loads(transcript_data)
                if 'segments' in data:
                    for seg in data['segments']:
                        if 'text' in seg:
                            segments.append({
                                'start': seg.get('start', 0),
                                'duration': seg.get('duration', 0),
                                'text': seg['text']
                            })
                    print(f"   Found {len(segments)} segments using JSON parsing")
                    return segments
        except:
            pass
        
        # Method 3: Look for any text content
        print("\n   Trying plain text extraction...")
        # Remove XML tags and extract text
        plain_text = re.sub(r'<[^>]+>', '', transcript_data)
        plain_text = plain_text.strip()
        
        if plain_text:
            # Split into rough segments
            text_lines = plain_text.split('\n')
            text_lines = [line.strip() for line in text_lines if line.strip()]
            
            if text_lines:
                # Create simple segments with equal timing
                total_duration = 60  # Assume 1 minute for simplicity
                segment_duration = total_duration / len(text_lines)
                
                for i, text in enumerate(text_lines):
                    segments.append({
                        'start': i * segment_duration,
                        'duration': segment_duration,
                        'text': text
                    })
                print(f"   Found {len(segments)} segments using plain text extraction")
                return segments
        
        print(f"   Found {len(segments)} segments")
        return segments
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    # Use a known video with subtitles if no URL provided
    if len(sys.argv) < 2:
        # Known video with subtitles: "Introduction to Python"
        video_url = 'https://www.youtube.com/watch?v=rfscVS0vtbw'
        print('Using default video with subtitles:', video_url)
        print('Usage: python simple-youtube-transcript.py <youtube_url>')
        print('Example: python simple-youtube-transcript.py https://www.youtube.com/watch?v=rfscVS0vtbw')
    else:
        video_url = sys.argv[1]
    
    video_id = extract_video_id(video_url)
    
    print(f"\n=== Simple YouTube Transcript Fetcher ===")
    print(f"Video URL: {video_url}")
    print(f"Video ID: {video_id}")
    print(f"Proxy: System default (ClashX global mode)")
    print()
    
    # Fetch transcript
    segments = fetch_transcript(video_id)
    
    if segments:
        print("\n=== Transcript Results ===")
        
        # Display first few segments
        print("\nFirst 10 segments:")
        for i, seg in enumerate(segments[:10], 1):
            mins = seg['start'] // 60
            secs = int(seg['start'] % 60)
            time_str = f"{mins}:{secs:02d}"
            print(f"[{time_str}] {seg['text']}")
        
        # Display full transcript
        print("\n--- Full Transcript ---")
        full_text = ' '.join([seg['text'] for seg in segments])
        print(full_text)
        
        # Summary
        print("\n=== Summary ===")
        print(f"Total segments: {len(segments)}")
        print(f"Transcript length: {len(full_text)} characters")
    else:
        print("\n❌ Failed to fetch transcript")
        print("\nPossible solutions:")
        print("1. Make sure ClashX is running in global mode")
        print("2. Verify proxy port 7890 is correct")
        print("3. Check if YouTube is accessible through your proxy")
        print("4. Ensure the video has available subtitles")

if __name__ == "__main__":
    main()