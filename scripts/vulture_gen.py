import json
import os

# Configuration
DATA_FILE = 'data/affiliate.json'
OUTPUT_DIR = 'pages'
TEMPLATE_FILE = 'index.html' # Uses your main style as a base

def generate_pages():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Load partner data
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    # Simple HTML Template for individual partner pages
    # Keeping your Deep Navy / Accent Cyan theme
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{name} | Nexus Stack Solutions</title>
        <style>
            body {{ background-color: #0a192f; color: #ccd6f6; font-family: sans-serif; text-align: center; padding: 100px; }}
            .container {{ max-width: 600px; margin: auto; background: #112240; padding: 50px; border-radius: 12px; border: 1px solid #64ffda; }}
            h1 {{ color: #e6f1ff; }}
            p {{ color: #8892b0; font-size: 1.2rem; }}
            .btn {{ display: inline-block; padding: 15px 30px; color: #64ffda; border: 1px solid #64ffda; text-decoration: none; font-weight: bold; margin-top: 20px; }}
            .btn:hover {{ background: rgba(100, 255, 218, 0.1); }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{name}</h1>
            <p><strong>{tagline}</strong></p>
            <p>{description}</p>
            <a href="{url}" class="btn">Access {name} via Nexus Stack →</a>
        </div>
    </body>
    </html>
    """

    for partner in data['partners']:
        filename = f"{partner['id']}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Fill template with partner data
        content = html_template.format(
            name=partner['name'],
            tagline=partner['tagline'],
            description=partner['description'],
            url=partner['url']
        )
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Generated: {filepath}")

if __name__ == "__main__":
    generate_pages()
