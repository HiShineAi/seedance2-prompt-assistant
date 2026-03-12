# 使用正确的 API 调用方式
from youtube_transcript_api import YouTubeTranscriptApi

# 创建实例
api = YouTubeTranscriptApi()

# 获取字幕
transcript = api.fetch(video_id, languages=['en', 'zh-Hans', 'zh-Hant'])

# 处理字幕
snippets = transcript.snippets
for snippet in snippets:
    print(f"[{format_time(snippet.start)}] {snippet.text}")