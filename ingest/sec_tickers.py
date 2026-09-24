import os
from datetime import date
from pathlib import Path

import requests
from dotenv import load_dotenv


URL = "https://www.sec.gov/files/company_tickers.json"

load_dotenv()
user_agent = os.getenv("SEC_USER_AGENT")
if not user_agent:
    raise SystemExit(
        "SEC_USER_AGENT is not set. Add a line to your .env file:\n"
        "SEC_USER_AGENT=Your Name your-email@example.com"
    )

# the SEC asks to let them know who we are
headers = {"User-Agent": user_agent}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()
data = response.json()
print(len(data))

out_dir = Path("data/raw/sec_company_tickers")
out_dir.mkdir(parents=True, exist_ok=True)

out_file = out_dir / f"{date.today()}.json"
out_file.write_bytes(response.content)
print(f"Saved to {out_file}")