# data-eng-project

An ELT pipeline for end-of-day US stock market data. Learning project covering Git, Docker, Postgres and dbt.

```
 Ingest (Python)        Load (Python)             Transform (dbt)
 call APIs      ──►     data/raw/*.json   ──►     raw.* tables  ──►  clean models
 save raw JSON          into Postgres             inside Postgres
```

## Repo layout

| Folder     | What lives there |
|------------|------------------|
| `ingest/`  | Extract: call the SEC and Massive APIs, save raw JSON to `data/raw/` |
| `load/`    | Load: insert the raw JSON into the `raw` schema in Postgres |
| `dbt/`     | Transform: SQL models that clean and join the raw tables |
| `docker/`  | `docker-compose.yml` that runs Postgres locally, plus first-run SQL in `docker/init/` |
| `data/`    | Local raw files (git-ignored, created by the ingest step) |

## First-time setup

1. Create your secrets file and set a password:
   ```bash
   cp .env.example .env
   ```
2. Start Postgres (Docker Desktop must be running):
   ```bash
   cd docker
   docker compose up -d
   ```
3. Connect with DBeaver: host `localhost`, port `5432`, database/user/password from your `.env`.
   You should see an empty `raw` schema.

## Python setup (once)

A *virtual environment* (`.venv/`) is a private copy of Python for this project,
so its packages don't clash with anything else on your Mac. From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate        # do this in every new Terminal window; prompt shows (.venv)
pip install -r requirements.txt
```

## Running the pipeline

```bash
source .venv/bin/activate
python ingest/sec_tickers.py     # company tickers -> data/raw/sec_company_tickers/
python ingest/daily_prices.py    # all US stock prices, last trading day -> data/raw/massive_daily_summary/
```

## Everyday Docker commands (run inside `docker/`)

| Command | What it does |
|---------|--------------|
| `docker compose up -d` | Start Postgres in the background |
| `docker compose ps` | Is it running / healthy? |
| `docker compose logs -f` | Watch the database logs (Ctrl+C to stop watching) |
| `docker compose down` | Stop Postgres — **data is kept** |
| `docker compose down -v` | Stop and **delete all data** (fresh start) |
