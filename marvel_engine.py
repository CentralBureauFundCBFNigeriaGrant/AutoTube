import os
from groq import Groq

# 1. Setup the Groq Client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Read your mission
with open("mission.txt", "r") as f:
    mission_content = f.read()

# 3. Ask Llama 3 to write the script
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are an expert YouTube script writer for a Marvel-themed channel."},
        {"role": "user", "content": f"Write a short, engaging video script based on this mission: {mission_content}"}
    ]
)

# 4. Save the result
script = completion.choices[0].message.content
with open("generated_script.md", "w") as f:
    f.write(script)

print("Script successfully generated using Llama 3!")
