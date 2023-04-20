import sys
import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def extract_subtitles(url):
    video_id = YouTube(url).video_id
    while True:
        try:
            title = YouTube(url).title
            GREEN = "\033[32m"
            RESET = "\033[0m"
            print(f"{GREEN}'Title: '{title}{RESET}")
            break
        except Exception as e:
            pass

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = ""
        for entry in transcript:
            subtitles += entry["text"] + " "

    except Exception as e:
        return e

    return title, subtitles
