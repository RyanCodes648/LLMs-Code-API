import os
from openai import OpenAI

# Initialize the client using the environment variable for security
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Chatbot initialized! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print('Chatbot: Goodbye!')
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

    