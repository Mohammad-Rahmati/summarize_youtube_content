import sys
import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def extract_subtitles(url):
    video_id = YouTube(url).video_id
    while True:
        try:
            title = YouTube(url).title
            print(f"Title: {title}")
            break
        except Exception as e:
            pass

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = ""
        for entry in transcript:
            subtitles += entry["text"] + " "

        if not os.path.exists("data"):
            os.makedirs("data")

        with open(f"data/{video_id}_subtitles.txt", "w", encoding="utf-8") as file:
            file.write(subtitles)

        print(f"Subtitles saved to {video_id}_subtitles.txt")

    except Exception as e:
        return e

    return video_id, title
