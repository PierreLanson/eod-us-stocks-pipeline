# ingest/

**E** of ELT — *Extract*.

Python code that calls the APIs and saves the raw responses to `data/raw/` as JSON files,
exactly as received (no cleaning here). Keeping the raw files means you can re-run the
load step without calling the API again.

Planned sources:
- SEC company tickers: https://www.sec.gov/files/company_tickers.json
  (every request needs a `User-Agent` header with your name + email — see `.env`)
- Massive (formerly Polygon.io) Daily Market Summary: OHLC + volume for every US stock for one date, in one call

## Scripts

| Script | What it does |
|--------|--------------|
| `sec_tickers.py` | Today's SEC ticker → CIK list, saved to `data/raw/sec_company_tickers/<date>.json` |
| `daily_prices.py` | Massive Daily Market Summary for one date (or a range with `--start/--end`), saved to `data/raw/massive_daily_summary/<date>.json` |
| `common.py` | Shared helpers: reads `.env`, builds `data/raw/...` paths |

Run `python ingest/daily_prices.py --help` for all options.
