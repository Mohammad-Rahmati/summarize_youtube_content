# Youtube Content Summarizer

This script is designed to download subtitles from a YouTube video, and then generate a summary in markdown format using OpenAI's GPT-3.5-turbo. The summary will be saved in an output directory as a markdown file.

## Instructions:

Ensure you have Python 3 installed.

Install the required packages using the command: `pip install -r requirements.txt`. The required packages are:

Set your OpenAI API Key as an environment variable, by running the command: 

`export OPENAI_API_KEY=your_api_key_here`. 

Replace your_api_key_here with your actual OpenAI API Key.

Run the script with the following command: `python main.py 'youtube_video_url'`. 

Replace your_script_name.py with the name of the script file, and youtube_video_url with the URL of the YouTube video you want to summarize.

The script will download the subtitles of the video, and save them in a data directory with the format: <video_id>_subtitles.txt.

The script will use GPT-3.5-turbo to generate a summary of the subtitles.

The summary will be saved in an output directory as a markdown file named summary.md.

If the bat command is available, the script will use it to display the summary in the terminal. Otherwise, it will try to open the file using the system's default text editor.

Please note that the OpenAI API Key is required to use GPT-3.5-turbo for summarizing the subtitles. If you do not have an OpenAI API Key, you will not be able to use this feature.
