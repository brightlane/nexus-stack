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

    # Professional Dark Blue Template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{name} | Nexus Stack Solutions</title>
        <style>
            body {{ background-color: #0a192f; color: #ccd6f6; font-family: sans-serif; line-height: 1.6; padding: 40px; }}
            .container {{ max-width: 800px; margin: auto; border: 1px solid #233554; padding: 30px; border-radius: 8px; }}
            h1 {{ color: #64ffda; }}
            .desc {{ font-size: 1.2rem; margin: 20px 0; color: #8892b0; }}
            .cta-btn {{ display: inline-block; padding: 15px 25px; background: transparent; border: 1px solid #64ffda; color: #64ffda; text-decoration: none; font-weight: bold; border-radius: 4px; }}
            .cta-btn:hover {{ background: rgba(100, 255, 218, 0.1); }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Expert Analysis: {name}</h1>
            <p class="desc">{description}</p>
            <a href="{url}" class="cta-btn">Access {name} Protocol →</a>
        </div>
    </body>
    </html>
    """

    for partner in data['partners']:
        # This fix uses .get() to prevent KeyError if 'tagline' or 'description' is missing
        description_text = partner.get('description', partner.get('tagline', 'Strategic infrastructure optimization active.'))
        
        filename = f"{partner['id']}-analysis.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        content = html_template.format(
            name=partner['name'],
            description=description_text,
            url=partner['url']
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Generated: {filepath}")

if __name__ == "__main__":
    generate_pages()
