import os
import google.generativeai as genai

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
    
    # Read the mission you typed in mission.txt
    try:
        with open('mission.txt', 'r') as f:
            mission = f.read().strip()
    except FileNotFoundError:
        mission = "No mission found. Defaulting to: Why AI is the future."

    # Run the AI logic
    script = generate_video_script(mission)
    
    # Save the output to a new file so you can see it
    with open('generated_script.md', 'w') as f:
        f.write(script)
    
    print("--- Success! Script generated in generated_script.md ---")

if __name__ == "__main__":
    main()
