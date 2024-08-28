# SimplePythonChatBot
This Chatbot uses the [Python OpenAI library](https://github.com/openai/openai-python) to let you chat with ChatGPT. You must provide your own API key if you want to use this script.

## Protection of API keys
To protect your API key, you should set it up as an environment variable. 
On Mac/Linux, type in this command:

`export OPENAI_API_KEY="api-key"`

On Windows, type in this command:

`set OPENAI_API_KEY="api-key"`

Make sure to replace "api-key" with the API key you got from OpenAI, which you can obtain [here](https://platform.openai.com/docs/overview), by signing up/logging in and clicking "API key reference", and also make sure to keep any ".env" files (that you got after the export) containing your API key not publicly visible. For example, if you are forking this repo, you may want to keep the key in GitHub secrets as a secret API key

## Installation
Before you go, remember that this script doesn't work with versions 1.0 and above of the Python OpenAI library (due to using a no-longer-supported feature), so when installing OpenAI, you must instead use the command:

`pip install openai==0.28`

in Terminal or Command Prompt.

### Script Overview
1. First, the script imports the OpenAI library.
2. Then, it inputs the API key.
3. After that, it defines a Python function to start chatting with you (look in the script).
4. Then, it checks if the Python script is being run directly. If true, the script then adds "You:" for your input and "Chatbot:" for the chatbot's response.
