#!/usr/bin/env python3
try:
    import sys
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    import os
    from dotenv import load_dotenv
    load_dotenv("/home/mo/Documents/summarize_youtube_content/.env")
    import openai
    from rich.console import Console
    from rich.markdown import Markdown
    from extract_subtitles import extract_subtitles
    import time
    import threading

except Exception as e:
    print("Some modules are missing. Installing the requirements...")
    try:
        os.system("pip install -r requirements.txt")
        print("\n\n\nrun the script again")

    except:
        print("error: ", e)

def waiting_animation() -> None:
    chars = "|/-\\"
    while True:
        for char in chars:
            sys.stdout.write(f"\r{char} Summarizing...")
            sys.stdout.flush()
            time.sleep(0.1)

def summarize_text(title: str, input_text: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI to summarize text in markdown format.",
            },
            {
                "role": "user",
                "content": "Generate a title as header and provide 10 bullet points short sentences \\\
                to summarize the following content in markdown format:" + input_text,
            },
        ],
    )

    summary = completion.choices[0]["message"]["content"]
    return summary

def main(url: str) -> None:

    openai.api_key = os.getenv("OPENAI_API_KEY")
    animation_thread = threading.Thread(target=waiting_animation)
    animation_thread.daemon = True
    title, input_text = extract_subtitles(url)
    animation_thread.start()
    animation_thread.join(0)

    summary = summarize_text(title, input_text)
    print('\n')
    console = Console()
    console.print(Markdown(summary))
    print('\n')
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        main(url)

    else:
        print("Please provide a URL as a command-line argument.")
