#!/usr/bin/env python3
try:
    import os
    import openai
    from rich.console import Console
    from rich.markdown import Markdown
    from extract_subtitles import extract_subtitles
    import sys

except Exception as e:
    print("Some modules are missing")
    try:
        os.system("pip install -r requirements.txt")
        print("\n\n\nrun the script again")
        exit()
    except:
        print("error: ", e)

openai.api_key = os.environ["OPENAI_API_KEY"]

def summarize_text(title, input_text):
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

def main(url):
    try:
        title, subtitles = extract_subtitles(url)

        print("Summarizing...")
        summary = summarize_text(title, subtitles)
        console = Console()
        console.print(Markdown(summary))
        print('\n')
    except Exception as e:
        print("error: ", e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        main(url)
    else:
        print("Please provide a URL as a command-line argument.")
