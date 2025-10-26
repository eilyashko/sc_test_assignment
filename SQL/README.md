Snowflake query helper

This folder contains a minimal Snowflake client and example usage. The client now supports querying any table within the configured `DATABASE.SCHEMA` (from `.env`).

Setup

- Create and activate a virtual environment (optional but recommended)
- Install dependencies:

```bash
pip install -r SQL/requirements.txt
```

- Create a `SQL/.env` file by copying `.env.example` and filling in values:

```bash
cp SQL/.env.example SQL/.env
```

Environment variables

Place these in `SQL/.env` (do not commit real secrets):

```bash
SNOWFLAKE_USER=HENRYMILLERINPARIS11
SNOWFLAKE_PASSWORD=REPLACE_ME
SNOWFLAKE_ACCOUNT=KHWLGYY-WI95230
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=SCALABLECAPITAL
SNOWFLAKE_SCHEMA=PUBLIC
SNOWFLAKE_ROLE=ACCOUNTADMIN
# Optional convenience for docs/examples; client does not require this
SNOWFLAKE_TABLE=CALLS
```

Python usage

```python
from SQL.snowflake_client import SnowflakeClient

with SnowflakeClient.from_env() as client:
    # Query any table in your configured database/schema
    df = client.table_to_df("CASES", limit=5)
    print(df.head())
```

Notebook usage

Open your notebook and use the `SnowflakeClient` to fetch rows from any table (e.g., `CASES`). The client automatically reads `SQL/.env` if present.

Notes

- Keep your real credentials only in `SQL/.env` (not tracked by git). The `.env.example` is safe to commit.
- If your table name differs, update the query accordingly or set `SNOWFLAKE_TABLE` and format your SQL string in the notebook.


