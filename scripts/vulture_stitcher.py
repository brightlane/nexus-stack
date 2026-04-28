import json
import os
import random

# Configuration
DATA_FILE = 'data/affiliate.json'
OUTPUT_DIR = 'blog'
FRAGMENTS_DIR = 'content_fragments'

def load_fragments(category):
    path = f"{FRAGMENTS_DIR}/fragments_{category.lower()}.txt"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            # Splits by double newline to get paragraphs
            return [p.strip() for p in f.read().split('\n\n') if p.strip()]
    return ["Standard business infrastructure optimization protocol active."]

def generate_blog_stack():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    # The HTML Master Template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title} | Nexus Stack Insights</title>
        <style>
            body {{ background-color: #0a192f; color: #ccd6f6; font-family: 'Inter', sans-serif; line-height: 1.8; padding: 40px; }}
            .article-container {{ max-width: 850px; margin: auto; background: #112240; padding: 60px; border-radius: 12px; border: 1px solid #233554; }}
            h1 {{ color: #e6f1ff; font-size: 2.5rem; }}
            .content-block {{ margin-bottom: 25px; font-size: 1.1rem; color: #8892b0; }}
            .cta-box {{ background: rgba(100, 255, 218, 0.05); border: 1px solid #64ffda; padding: 30px; border-radius: 8px; margin: 40px 0; text-align: center; }}
            .btn {{ display: inline-block; padding: 15px 35px; color: #64ffda; border: 1px solid #64ffda; text-decoration: none; font-weight: bold; border-radius: 4px; }}
            .btn:hover {{ background: rgba(100, 255, 218, 0.1); }}
        </style>
    </head>
    <body>
        <div class="article-container">
            <h1>{title}</h1>
            <div class="content-block">{p1}</div>
            <div class="content-block">{p2}</div>
            
            <div class="cta-box">
                <h2>{name} Solutions</h2>
                <p>{description}</p>
                <a href="{url}" class="btn">Optimize Your {pillar} Strategy →</a>
            </div>

            <div class="content-block">{p3}</div>
            <div class="content-block">{p4}</div>
            <div class="content-block">{p5}</div>
        </div>
    </body>
    </html>
    """

    for partner in data['partners']:
        # Load fragments for this specific niche
        fragments = load_fragments(partner['pillar'])
        
        # Randomly select 5 fragments to ensure page uniqueness
        selected = random.sample(fragments, min(len(fragments), 5))
        # If not enough fragments, pad with general ones
        while len(selected) < 5:
            selected.append("Strategic implementation of high-scale digital infrastructure ensures long-term market dominance.")

        filename = f"{partner['id']}-analysis.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        content = html_template.format(
            title=f"The Future of {partner['pillar']}: {partner['name']} Integration",
            name=partner['name'],
            pillar=partner['pillar'],
            description=partner['description'],
            url=partner['url'],
            p1=selected[0],
            p2=selected[1],
            p3=selected[2],
            p4=selected[3],
            p5=selected[4]
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Build complete: {filepath}")

if __name__ == "__main__":
    generate_blog_stack()
