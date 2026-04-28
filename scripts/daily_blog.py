import json
import os
import random
from datetime import datetime

# Configuration
DATA_FILE = 'data/affiliate.json'
FRAGMENTS_DIR = 'content_fragments'
OUTPUT_DIR = 'daily-updates'

def generate_daily_post():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 1. Load a random partner to feature
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    partner = random.choice(data['partners'])

    # 2. Load fragments for that partner's niche
    path = f"{FRAGMENTS_DIR}/fragments_{partner['pillar'].lower()}.txt"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            fragments = [p.strip() for p in f.read().split('\n\n') if p.strip()]
    else:
        fragments = ["Infrastructure optimization is the core of modern digital growth."]

    selected = random.sample(fragments, min(len(fragments), 2))
    date_str = datetime.now().strftime("%Y-%m-%d")
    title = f"Operations Update: {partner['pillar']} Optimization"
    
    # 3. Create the HTML
    content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{ background-color: #0a192f; color: #ccd6f6; font-family: sans-serif; line-height: 1.8; padding: 50px; }}
            .post {{ max-width: 800px; margin: auto; background: #112240; padding: 40px; border-radius: 10px; border: 1px solid #233554; }}
            h1 {{ color: #64ffda; }}
            .cta {{ border: 1px dashed #64ffda; padding: 20px; margin-top: 30px; text-align: center; }}
            a {{ color: #64ffda; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="post">
            <p><small>{date_str} // DAILY PROTOCOL UPDATE</small></p>
            <h1>{title}</h1>
            <p>{selected[0]}</p>
            <div class="cta">
                <p><strong>Featured Solution:</strong> {partner['name']}</p>
                <a href="{partner['url']}">Learn More about {partner['pillar']} Optimization →</a>
            </div>
            {"<p>" + selected[1] + "</p>" if len(selected) > 1 else ""}
        </div>
    </body>
    </html>
    """

    filename = f"post-{date_str}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(content)
    
    print(f"Daily post generated: {filename}")
    return title, filename  # This line fixes the NameError

if __name__ == "__main__":
    generate_daily_post()
