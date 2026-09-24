import os
import json
from pathlib import Path

import psycopg
from dotenv import load_dotenv


# Read the Postgres settings from .env
load_dotenv()
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
dbname = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

# Load hard coded data - this will change to updating date
path = Path("data/raw/massive_daily_summary/2026-09-23.json")
data = json.loads(path.read_text())
trading_date = path.stem
source_file = "massive_daily_summary/2026-09-23.json"

# Copy the metadata of massive.com 
rows = [
    (
        item["T"],          # ticker - always present
        item["o"],          # open
        item["h"],          # high
        item["l"],          # low
        item["c"],          # close
        item["v"],          # volume
        item.get("vw"),     # VWAP - can be missing → None → NULL
        item.get("n"),      # number of trades - can be missing
        item["t"],          # timestamp (ms)
        trading_date,
        source_file,
    )
    for item in data["results"]
]
print(len(rows))

# Remove duplicates before updating table - stopping duplicate data if ran more than once in a day
DELETE_SQL = "DELETE FROM raw.massive_daily_summary WHERE source_file = %s"

INSERT_SQL = """
    INSERT INTO raw.massive_daily_summary
        ("T", o, h, l, c, v, vw, n, t, trading_date, source_file)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Details from .emv file, delete old, insert new 
with psycopg.connect(host=host, port=port, dbname=dbname, user=user, password=password) as conn:
    with conn.cursor() as cur:
        cur.execute(DELETE_SQL, (source_file,))
        cur.executemany(INSERT_SQL, rows)

print(f"Loaded {len(rows)} rows from {source_file}")
