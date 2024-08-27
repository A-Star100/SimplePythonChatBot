import openai
import os

# Set up the API key as an environment variable for added security by referring to the README.
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_Input = input("You: ")
        if user_Input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_Input)
        print("Chatbot: ", response)
