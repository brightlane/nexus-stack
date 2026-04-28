import json
import os

# Configuration
DATA_FILE = 'data/affiliate.json'
OUTPUT_DIR = 'blog'

def generate_pages():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    # Professional Navy Blue Template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{name} | Nexus Stack</title>
        <style>
            body {{ background-color: #0a192f; color: #ccd6f6; font-family: sans-serif; padding: 40px; }}
            .container {{ max-width: 800px; margin: auto; border: 1px solid #233554; padding: 30px; border-radius: 8px; }}
            h1 {{ color: #64ffda; }}
            .text {{ color: #8892b0; margin: 20px 0; }}
            .cta {{ display: inline-block; padding: 12px 20px; border: 1px solid #64ffda; color: #64ffda; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{name} Analysis</h1>
            <p class="text">{content_text}</p>
            <a href="{url}" class="cta">Deploy Protocol →</a>
        </div>
    </body>
    </html>
    """

    for partner in data['partners']:
        # FIX: Check for 'description' first, then 'tagline', then a default string
        content_text = partner.get('description', partner.get('tagline', 'Strategic optimization in progress.'))
        
        filename = f"{partner['id']}-analysis.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Apply the fix to the formatting
        content = html_template.format(
            name=partner['name'],
            content_text=content_text,
            url=partner.get('url', '#')
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
    print(f"Vulture 10K: Successfully generated pages for {len(data['partners'])} partners.")

if __name__ == "__main__":
    generate_pages()
