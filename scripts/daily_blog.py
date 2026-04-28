import json
import os
import random
import tweepy # Add this to your requirements.txt
from datetime import datetime

# ... (keep your existing generate_daily_post() logic) ...

def post_to_social(title, link):
    # Get credentials from GitHub Secrets (Environment Variables)
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_secret = os.getenv("X_ACCESS_SECRET")

    if not all([api_key, api_secret, access_token, access_secret]):
        print("Social Media keys missing. Skipping post.")
        return

    # Authenticate with X
    client = tweepy.Client(
        consumer_key=api_key, consumer_secret=api_secret,
        access_token=access_token, access_token_secret=access_secret
    )

    # Create the post
    tweet_text = f"🚀 New Ops Update: {title}\n\nRead more at Nexus Stack: {link}\n\n#NexusStack #Automation #pSEO #2026"
    
    try:
        client.create_tweet(text=tweet_text)
        print("✅ Successfully posted to X!")
    except Exception as e:
        print(f"❌ Failed to post to X: {e}")

if __name__ == "__main__":
    # 1. Generate the blog post
    title, filename = generate_daily_post() # Modified to return title/filename
    
    # 2. Post the live link to social media
    live_url = f"https://brightlane.github.io/nexus-stack/daily-updates/{filename}"
    post_to_social(title, live_url)
