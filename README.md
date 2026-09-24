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

## Everyday Docker commands (run inside `docker/`)

| Command | What it does |
|---------|--------------|
| `docker compose up -d` | Start Postgres in the background |
| `docker compose ps` | Is it running / healthy? |
| `docker compose logs -f` | Watch the database logs (Ctrl+C to stop watching) |
| `docker compose down` | Stop Postgres — **data is kept** |
| `docker compose down -v` | Stop and **delete all data** (fresh start) |
