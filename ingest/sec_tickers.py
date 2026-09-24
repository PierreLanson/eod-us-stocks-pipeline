from datetime import date
from pathlib import Path

import requests



URL = "https://www.sec.gov/files/company_tickers.json"

# the SEC asks to let them know who we are (will add this to the .emv)
headers = {"User-Agent": "Pierre Lanson pierrelanson@protonmail.com"}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()
data = response.json()



print(len(data))

out_dir = Path("data/raw/sec_company_tickers")
out_dir.mkdir(parents=True, exist_ok=True)

out_file = out_dir / f"{date.today()}.json"
out_file.write_bytes(response.content)
print(f"Saved to {out_file}")