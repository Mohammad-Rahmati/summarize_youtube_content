# Youtube Content Summarizer

This script is designed to download subtitles from a YouTube video, and then generate a summary in markdown format using OpenAI's GPT-3.5-turbo. The summary will be saved in an output directory as a markdown file.

![image](https://user-images.githubusercontent.com/22165051/233439941-128ef583-13c4-4018-b192-92c696e140cc.png)

![image](https://user-images.githubusercontent.com/22165051/233443541-9093f56f-6135-46aa-9900-463e85f9531d.png)


## Instructions:

Ensure you have Python 3 installed.

Install the required packages using the command: `pip install -r requirements.txt`. The required packages are:

Set your OpenAI API Key as an environment variable, by running the command: 

`export OPENAI_API_KEY=your_api_key_here`. 

Run the script with the following command: `python main.py 'youtube_video_url'`.

The script will use GPT-3.5-turbo to generate a summary of the subtitles.

Please note that the OpenAI API Key is required to use GPT-3.5-turbo for summarizing the subtitles. If you do not have an OpenAI API Key, you will not be able to use this feature. Note that using OpenAI API is not free.
