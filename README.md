# 🚀 Printify SEO Engine (Programmatic Affiliate Network)

A high-velocity, automated content generation engine designed to dominate Bing search results for Printify-related long-tail keywords. This project uses a **10-into-1 content strategy** and the **IndexNow protocol** to achieve instant indexing and high conversion rates.

## 🛠 Project Architecture
- **Framework:** Programmatic HTML/CSS (Glassmorphism UI)
- **Automation:** GitHub Actions (Cron @ 00:00 UTC)
- **Engine:** Python 3.10 + Pandas
- **Target:** 1,000+ High-intent keywords for [Printify](https://try.printify.com/r3xsnwqufe8t)
- **SEO:** Bing IndexNow API + Dynamic XML Sitemaps

## 📂 Repository Structure
- `/sites/`: Contains the programmatically generated deep-pages.
- `generator.py`: The core Python engine that builds sites and updates the database.
- `keywords.csv`: The master keyword ledger (Pending/Completed status).
- `sitemap.xml`: Auto-updating map for search engine crawlers.
- `robots.txt`: Optimized crawler instructions.
- `.github/workflows/`: Automation logic for daily site rollouts.

## ⚡ Deployment Instructions

### 1. Setup Secrets
In your GitHub Repository, go to `Settings > Secrets and variables > Actions` and add:
- `INDEXNOW_KEY`: Your 32-character Bing IndexNow API key.

### 2. Permissions
Ensure the repository has Write permissions for the Action Bot:
- `Settings > Actions > General > Workflow permissions` -> Select **Read and write permissions**.

### 3. Local Generation (Optional)
To trigger the engine manually without waiting for the Cron job:
```bash
python generator.py
