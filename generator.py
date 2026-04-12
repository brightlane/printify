import pandas as pd
import os
import requests
import datetime

# --- CONFIG ---
AFFILIATE_URL = "https://try.printify.com/r3xsnwqufe8t"
INDEXNOW_KEY = os.getenv("INDEXNOW_KEY")
HOST = "brightlane.github.io"

def run_automation():
    # 1. Handle CSV creation if first run
    if not os.path.exists('keywords.csv'):
        print("CSV missing. Generating new keyword database...")
        # (Insert your 1000-keyword generation logic here)
        return 

    try:
        df = pd.read_csv('keywords.csv')
        
        # 2. Get next batch
        batch = df[df['status'] == 'pending'].head(10)
        if batch.empty:
            print("Job complete. All 1000 keywords indexed.")
            return

        new_urls = []
        for index, row in batch.iterrows():
            kw = row['keyword']
            # Create the folder and HTML (simplified for example)
            slug = kw.replace(" ", "-")
            os.makedirs(f"sites/{slug}", exist_ok=True)
            
            # Write your beautiful Glassmorphism HTML here
            with open(f"sites/{slug}/index.html", "w") as f:
                f.write(f"<h1>{kw}</h1><a href='{AFFILIATE_URL}'>Buy Now</a>")
            
            new_urls.append(f"https://{HOST}/sites/{slug}/")
            df.at[index, 'status'] = 'completed'
            df.at[index, 'date_launched'] = datetime.date.today().isoformat()

        # 3. Save and Ping
        df.to_csv('keywords.csv', index=False)
        
        if INDEXNOW_KEY:
            resp = requests.post("https://www.bing.com/indexnow", json={
                "host": HOST, "key": INDEXNOW_KEY, "keyLocation": f"https://{HOST}/{INDEXNOW_KEY}.txt", "urlList": new_urls
            })
            print(f"Bing Ping Status: {resp.status_code}")

    except Exception as e:
        print(f"Automation failed: {e}")

if __name__ == "__main__":
    run_automation()
