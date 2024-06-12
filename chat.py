from openai import OpenAI
import os

# Ysk-proj-4AABIYPFfxSjVPfNzlZrT3BlbkFJm21MURVcc0cGBNBlECen

assistant_name = "My Assistant"
assistant_description = "A helpful assistant for various tasks"
model = "gpt-4-1106-preview"  


def chat_with_gpt(prompt):
    apiKey = os.getenv("OPENAI_API_KEY")
    print(os.environ)
    print("Chatbot: ", apiKey)
    client = OpenAI(api_key=apiKey)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user","content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)