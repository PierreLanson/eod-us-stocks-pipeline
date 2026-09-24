-- Runs automatically the FIRST time the Postgres container starts
-- (i.e. only when the data volume is empty). Changing this file later has no
-- effect unless you reset the database: docker compose down -v  (deletes all data!)

-- raw: tables loaded exactly as they come from the APIs (the "L" in ELT)
CREATE SCHEMA IF NOT EXISTS raw;
