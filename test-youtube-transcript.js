#!/usr/bin/env node

/**
 * YouTube Transcript Fetcher with Proxy Support
 * Test script to demonstrate the fix
 */

// Set proxy environment variables
process.env.HTTP_PROXY = 'http://127.0.0.1:7890';
process.env.HTTPS_PROXY = 'http://127.0.0.1:7890';
process.env.http_proxy = 'http://127.0.0.1:7890';
process.env.https_proxy = 'http://127.0.0.1:7890';

const { YoutubeTranscript } = require('youtube-transcript');

function extractVideoId(url) {
  // Handle various YouTube URL formats
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)([^&\n?#]+)/,
  ];

  for (const pattern of patterns) {
    const match = url.match(pattern);
    if (match) {
      return match[1];
    }
  }
  return url; // Return as-is if it's already a video ID
}

async function fetchTranscript(videoUrl, options = {}) {
  const videoId = extractVideoId(videoUrl);

  try {
    console.log(`Fetching transcript for video ID: ${videoId}`);
    console.log(`Using proxy: ${process.env.HTTPS_PROXY}`);

    // Try to fetch transcript with language preferences
    const transcript = await YoutubeTranscript.fetchTranscript(videoId, {
      lang: options.lang || ['zh-Hans', 'zh-Hant', 'en', 'en-US', 'ja'],
    });

    // Format transcript
    let fullText = '';
    const segments = transcript.map((segment, index) => {
      const time = formatTime(segment.offset);
      fullText += segment.text + ' ';
      return `[${time}] ${segment.text}`;
    });

    return {
      videoId,
      videoUrl: `https://www.youtube.com/watch?v=${videoId}`,
      segments,
      fullText: fullText.trim(),
      segmentCount: transcript.length,
    };
  } catch (error) {
    if (error.message.includes('Could not retrieve transcript')) {
      throw new Error(`此视频没有可用的字幕。`);
    }
    throw error;
  }
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}

// CLI usage
if (require.main === module) {
  const videoUrl = process.argv[2] || 'https://www.youtube.com/watch?v=vCoGfisdS8Y';

  console.log(`
=== YouTube Transcript Fetcher ===`);
  console.log(`Video URL: ${videoUrl}`);
  console.log(`Proxy: ${process.env.HTTPS_PROXY}
`);

  fetchTranscript(videoUrl)
    .then((result) => {
      console.log(`✅ Success!`);
      console.log(`Video: ${result.videoUrl}`);
      console.log(`Segments: ${result.segmentCount}\n`);
      console.log(result.segments.join('\n'));
      console.log('\n=== Full Text ===\n');
      console.log(result.fullText);
    })
    .catch((error) => {
      console.error('❌ Error:', error.message);
      console.log('\nPossible solutions:');
      console.log('1. Make sure ClashX is running in global mode');
      console.log('2. Verify proxy port 7890 is correct');
      console.log('3. Check if YouTube is accessible through your proxy');
      process.exit(1);
    });
}

module.exports = { fetchTranscript, extractVideoId };