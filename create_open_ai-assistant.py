import time
from openai import OpenAI
from dotenv import load_dotenv
import os


# pip install beautifulsoup4 requests pandas

# pip install openai --upgrade

# pip install python-dotenv





# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Use the environment variable in your script
client = OpenAI(api_key=OPENAI_API_KEY)

# Create the assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a math tutor capable of writing and running code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# Create a thread
thread = client.beta.threads.create()
print(thread)

# Send a message in the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Answer specific questions: 5 * 5 + 9"
)
print(message)

# Create a run to execute the assistant's response
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Wait for the run to complete
import time

# Assuming a wait loop is necessary; modify the condition based on actual SDK usage
while True:
    run_result = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id,
    )
    if run_result.status == "completed":
        break
    elif run_result.status == "failed":
        print("Run failed. Check the error logs.")
        break
    time.sleep(2)  # Wait a bit before checking again

# List all messages in the thread
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

# Print all messages
for message in reversed(messages.data):
    content = message.content
    if isinstance(content, list):
        # Extract the text from each block and join them into a single string
        content = ''.join([block.text.value for block in content])
    print(message.role + ": " + content)