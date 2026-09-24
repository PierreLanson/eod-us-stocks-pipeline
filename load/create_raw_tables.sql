CREATE TABLE IF NOT EXISTS raw.massive_daily_summary (
    -- fields from the API, names kept exactly as Massive sends them
    "T"            text             NOT NULL,
    o              numeric,
    h              numeric,
    l              numeric,
    c              numeric,
    v              numeric,
    vw             numeric,
    n              bigint,
    t              bigint           NOT NULL,

    -- context we add when loading
    trading_date   date             NOT NULL,
    source_file    text             NOT NULL,
    loaded_at      timestamptz      NOT NULL DEFAULT now()
);


CREATE TABLE IF NOT EXISTS raw.sec_company_tickers (
    -- fields from the API, names kept exactly as sec sends them
    cik_str        bigint           NOT NULL,
    ticker         text             NOT NULL,
    title          text,

    -- context we add when loading
    snapshot_date  date             NOT NULL,
    source_file    text             NOT NULL,
    loaded_at      timestamptz      NOT NULL DEFAULT now()
);
