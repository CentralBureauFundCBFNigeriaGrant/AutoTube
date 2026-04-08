import os

def main():
    print("--- Marvel Engine Activated ---")
    print("Mission Received: 10 Secrets of Going Viral")
    
    # This just checks if your secrets are working
    gemini_key = os.getenv('GEMINI_API_KEY')
    if gemini_key:
        print("Status: Gemini API Key is loaded.")
    else:
        print("Status: Gemini API Key is missing!")

if __name__ == "__main__":
    main()
  
