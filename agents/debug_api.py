import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("AI_MODEL", "meta-llama/llama-3-8b-instruct:free")

print(f"[*] Testing OpenRouter Connection...")
print(f"[*] API Key: {api_key[:10]}...{api_key[-5:] if api_key else ''}")
print(f"[*] Model: {model}")

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://praedix.ai", 
    "X-Title": "Praedix AI Security", 
}

data = {
    "model": model,
    "messages": [
        {"role": "user", "content": "Hello, are you online?"}
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"\n[+] HTTP Status: {response.status_code}")
    print(f"[+] Response Text: \n{response.text}")
except Exception as e:
    print(f"\n[!] Connection Error: {e}")
