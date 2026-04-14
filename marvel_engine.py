import requests
import json

# 1. Your specific Make.com Webhook URL
WEBHOOK_URL = "https://hook.us2.make.com/0slt5wk6nbkp41mi4463ep3tx2lpfklj"

def send_to_make(mission_data, script_data):
    """Sends the generated content to Make.com with robust error checking."""
    
    payload = {
        "mission": mission_data,
        "script": script_data
    }

    print(f"--- Sending data to Make.com ---")
    
    try:
        # We add a standard User-Agent header to prevent being blocked as a bot
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0" 
        }

        # Sending the POST request
        response = requests.post(
            WEBHOOK_URL, 
            data=json.dumps(payload), 
            headers=headers,
            timeout=30
        )

        # This will print the status in your GitHub Actions log
        if response.status_code == 200 or response.text == "Accepted":
            print(f"✅ SUCCESS: Data received by Make.com. Status: {response.status_code}")
            print(f"Response body: {response.text}")
        else:
            print(f"❌ FAILED: Make.com returned status {response.status_code}")
            print(f"Response detail: {response.text}")

    except Exception as e:
        print(f"🚨 CRITICAL ERROR: Could not connect to the webhook. Reason: {e}")

# --- Trigger the function inside your existing script flow ---
# send_to_make(mission, script) 

start
