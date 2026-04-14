import os
import google.generativeai as genai
import requests  # Added to send data to your webhook

def generate_video_script(mission_text):
    # Setup Gemini API
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return "Error: GEMINI_API_KEY is not set in GitHub Secrets."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    You are Marvel, an expert YouTube Automation Engine.
    I have a mission: {mission_text}
    
    Create a high-retention YouTube script for a faceless video.
    Include:
    1. A 'hook' for the first 5 seconds.
    2. 10 clear, engaging points.
    3. A call to action at the end.
    Keep the tone viral and energetic.
    """

    print(f"--- Processing Mission: {mission_text} ---")
    response = model.generate_content(prompt)
    return response.text

def main():
    print("--- Marvel Engine Activated ---")
    
    # Your Make.com Webhook URL
    WEBHOOK_URL = "https://hook.us2.make.com/0slt5wk6nbkp41mi4463ep3tx2lpfklj"
    
    # Read the mission you typed in mission.txt
    try:
        with open('mission.txt', 'r') as f:
            mission = f.read().strip()
    except FileNotFoundError:
        mission = "No mission found. Defaulting to: Why AI is the future."

    # Run the AI logic
    script = generate_video_script(mission)
    
    # 1. Save the output locally (as a backup)
    with open('generated_script.md', 'w') as f:
        f.write(script)
    
    # 2. Send the script to Make.com Webhook
    print(f"--- Sending data to Make.com ---")
    payload = {
        "mission": mission,
        "script": script
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print("--- Success! Data received by Make.com ---")
        else:
            print(f"--- Webhook Error: {response.status_code} ---")
    except Exception as e:
        print(f"--- Failed to connect to Webhook: {e} ---")

    print("--- Process Complete! ---")

if __name__ == "__main__":
    main()
Now
