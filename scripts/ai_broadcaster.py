import json
import os
import requests
from datetime import datetime

def broadcast_to_ai_networks(title, url):
    api_key = os.getenv("AYRSHARE_API_KEY")
    if not api_key:
        print("API Key missing. Skipping broadcast.")
        return

    # The payload for 2026 AI networks
    payload = {
        "post": f"🚀 NEXUS STACK UPDATE: {title}\n\nOur Vulture 10K Engine has deployed new operational insights. Access the full stack here: {url}\n\n#NexusStack #Automation #pSEO #AI2026",
        "platforms": ["twitter", "linkedin", "facebook", "instagram", "threads"],
        "shortenLinks": True
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.ayrshare.com/api/post", json=payload, headers=headers)
    
    if response.status_code == 200:
        print("✅ Successfully broadcasted to the AI ecosystem.")
    else:
        print(f"❌ Broadcast failed: {response.text}")

if __name__ == "__main__":
    # Get the most recent post info
    date_str = datetime.now().strftime("%Y-%m-%d")
    post_title = f"Daily Operations Protocol - {date_str}"
    post_url = f"https://brightlane.github.io/nexus-stack/daily-updates/post-{date_str}.html"
    
    broadcast_to_ai_networks(post_title, post_url)
