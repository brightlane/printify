import os
import random
import requests
import datetime

# --- CONFIGURATION ---
AFFILIATE_URL = "https://try.printify.com/r3xsnwqufe8t"
INDEXNOW_KEY = os.getenv("INDEXNOW_KEY") # Pulled from GitHub Secrets
HOST = "brightlane.github.io" # Your domain

def create_site(keyword, index):
    """Generates the 3000-word HTML file based on your beautiful template."""
    # (Insert the Beautiful UI CSS & HTML logic from our previous steps here)
    html_content = f"<html>... {keyword} ... {AFFILIATE_URL} ...</html>"
    
    path = f"output/site-{index}"
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/index.html", "w") as f:
        f.write(html_content)
    
    return f"https://{HOST}/site-{index}/index.html"

def ping_bing(urls):
    """Notifies Bing to index the new content immediately."""
    data = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://{HOST}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    requests.post("https://www.bing.com/indexnow", json=data)

# --- EXECUTION ---
if __name__ == "__main__":
    keywords = ["custom hoodies", "print on demand shirts", "eco-friendly mugs"] # Pull from your 1000 keyword list
    new_urls = []
    
    for i in range(10):
        kw = random.choice(keywords)
        url = create_site(kw, i + (datetime.datetime.now().day * 10))
        new_urls.append(url)
    
    ping_bing(new_urls)
    print(f"Successfully deployed 10 sites and pinged Bing.")
