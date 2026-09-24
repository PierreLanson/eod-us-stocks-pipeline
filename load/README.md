# load/

**L** of ELT — *Load*.

Python code that reads the JSON files in `data/raw/` and inserts them, untransformed,
into tables in the `raw` schema of Postgres (e.g. `raw.sec_company_tickers`, `raw.daily_prices`).
