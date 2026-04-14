import os
from groq import Groq

# 1. Initialize the Groq Client
# This uses the secret key you just saved in your GitHub settings
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your GitHub Secrets.")

client = Groq(api_key=api_key)

def generate_marvel_script():
    # 2. Read the mission from your mission.txt file
    try:
        with open("mission.txt", "r") as f:
            mission_content = f.read().strip()
    except FileNotFoundError:
        print("Error: mission.txt file not found in the repository.")
        return

    if not mission_content:
        print("mission.txt is empty. Please add a mission description.")
        return

    print(f"Starting Llama 3 engine for mission: {mission_content}")

    # 3. Call the Groq API (Llama 3 8B Model)
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a viral YouTube scriptwriter. Write engaging, cinematic scripts for Marvel fans."
                },
                {
                    "role": "user", 
                    "content": f"Create a detailed YouTube video script for this topic: {mission_content}"
                }
            ],
            temperature=0.7
        )

        # 4. Save the generated script
        script_output = completion.choices[0].message.content
        
        with open("generated_script.md", "w") as f:
            f.write(script_output)
            
        print("Done! Script saved to generated_script.md")

    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    generate_marvel_script()
    
