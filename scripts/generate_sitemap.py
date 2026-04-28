import os
from datetime import datetime

# Configuration
BASE_URL = "https://brightlane.github.io/nexus-stack/"
PAGES_DIR = "pages"
SITEMAP_FILE = "sitemap.xml"

def generate_sitemap():
    # Start the XML structure
    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    # 1. Add the Home Page
    now = datetime.now().strftime("%Y-%m-%d")
    sitemap_content.append(f"  <url>")
    sitemap_content.append(f"    <loc>{BASE_URL}</loc>")
    sitemap_content.append(f"    <lastmod>{now}</lastmod>")
    sitemap_content.append(f"    <priority>1.0</priority>")
    sitemap_content.append(f"  </url>")

    # 2. Add all generated pages
    if os.path.exists(PAGES_DIR):
        for filename in os.listdir(PAGES_DIR):
            if filename.endswith(".html"):
                page_path = f"{BASE_URL}pages/{filename}"
                sitemap_content.append(f"  <url>")
                sitemap_content.append(f"    <loc>{page_path}</loc>")
                sitemap_content.append(f"    <lastmod>{now}</lastmod>")
                sitemap_content.append(f"    <priority>0.8</priority>")
                sitemap_content.append(f"  </url>")

    # Close the XML
    sitemap_content.append('</urlset>')

    # Write the file
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_content))
    
    print(f"✅ Sitemap successfully generated at {SITEMAP_FILE}")

if __name__ == "__main__":
    generate_sitemap()
