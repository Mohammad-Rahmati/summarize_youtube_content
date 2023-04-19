#!/usr/bin/env python3
try:
    import os
    import openai
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
        video_id, title = extract_subtitles(url)

        with open(f"data/{video_id}_subtitles.txt", "r") as file:
            input_text = file.read()
        
        print("Summarizing...")
        summary = summarize_text(title, input_text)

        if not os.path.exists("output"):
            os.makedirs("output")

        with open("output/summary.md", "w") as file:
            file.write(summary)

        print("Summary saved to output/summary.md")

        try:
            os.system("bat output/summary.md")
        except:
            os.system("open output/summary.md")

    except Exception as e:
        print("error: ", e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        main(url)
    else:
        print("Please provide a URL as a command-line argument.")
