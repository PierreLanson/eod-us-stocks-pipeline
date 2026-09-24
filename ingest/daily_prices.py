import os
from pathlib import Path
from datetime import date, timedelta

import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("MASSIVE_API_KEY")
if not api_key:
    raise SystemExit(...)   # your message from above


trading_date = date.today() - timedelta(days=1)
url = f"https://api.massive.com/v2/aggs/grouped/locale/us/market/stocks/{trading_date}"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers, params={"adjusted": "true"}, timeout=60)
response.raise_for_status()
data = response.json()

if not data.get("resultsCount", 0):
    print(f"No results for {trading_date} - the markets were closed, or data not published yet. Nothing saved.")
    raise SystemExit(0)

# --- Save the raw response ---
out_dir = Path("data/raw/massive_daily_summary")
out_dir.mkdir(parents=True, exist_ok=True)

out_file = out_dir / f"{trading_date}.json"
out_file.write_bytes(response.content)
print(f"Saved {data['resultsCount']} stocks to {out_file}")