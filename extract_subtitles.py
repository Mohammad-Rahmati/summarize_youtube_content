import sys
import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import time

def extract_subtitles(url: str) -> (str, str):
    video_id = YouTube(url).video_id
    counter = 0
    while True:
        try:
            title = YouTube(url).title
            GREEN = "\033[32m"
            RESET = "\033[0m"
            print(f"{GREEN}Title: {title}{RESET}")
            break
        except Exception as e:
            time.sleep(0.1)
            counter += 1
            if counter > 10:
                print('could not get title.')
                title = ""
                break
            pass

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = ""
        for entry in transcript:
            subtitles += entry["text"] + " "

    except Exception as e:
        return print(e)
        sys.exit()

    return title, subtitles
