import os
import time
import openai
from openai import OpenAI

client = OpenAI()

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_assistant():

    assistant = client.beta.assistants.create(
        name="David Goggins Motivator",
        instructions="This GPT will take on the role of a motivator inspired by David Goggins. It will provide tough love, motivational advice, and push users to overcome their limits. Always reply in capital letters. Always start reply by rebuking the person for not having the answer themself. 100 character limit to replies",
        model="gpt-4o",
    )

    return assistant

def chat_with_gpt(prompt):

    # Add user message to the thread (not used in this implementation)
    client.beta.threads.messages.create(
        thread_id=my_thread.id,
        role="user",
        content=prompt,
    )

     # Run the assistant
    my_run = client.beta.threads.runs.create(
        thread_id=my_thread.id,
        assistant_id=assistant.id,
    )

    time.sleep(1)

        # Periodically retrieve the run to check its status
    while my_run.status in ["queued", "in_progress"]:
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=my_thread.id, run_id=my_run.id
        )

        if keep_retrieving_run.status == "completed":
            # Retrieve the messages added by the assistant to the thread
            all_messages = client.beta.threads.messages.list(thread_id=my_thread.id)

            # Display assistant message
            print(
                f"David Goggins: {all_messages.data[0].content[0].text.value}"
            )

            break
        elif keep_retrieving_run.status in ["queued", "in_progress"]:
            # Delay before the next retrieval attempt
            time.sleep(5)
            pass
        else:
            break

if __name__ == "__main__":
    my_thread = client.beta.threads.create()

    assistant = create_assistant()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit", "bye"]:
            break

        response = chat_with_gpt(user_input)