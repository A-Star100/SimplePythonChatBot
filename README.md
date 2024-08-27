# SimplePythonChatBot
This Chatbot uses the Python OpenAI library to chat with ChatGPT. You must provide your own API key if you want to use this script.

## Important
Before you go, remember that this script doesn't work with versions 1.0 and above of the Python OpenAI library, so when installing OpenAI, you must instead use the command:

`pip install openai==0.28`

in Terminal.

### Script Overview
1. First, the script imports the OpenAI library.
2. Then, it inputs the API key.
3. After that, it defines a Python function to start chatting with you (look in the script).
4. Then, it checks if the Python script is being run directly. If true, the script then adds "You:" for your input and "Chatbot:" for the chatbot's input.
