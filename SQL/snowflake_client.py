import os
from pathlib import Path
from typing import Any, Optional, Sequence

import pandas as pd
from dotenv import load_dotenv
import snowflake.connector as sf


class SnowflakeClient:
    """Lightweight Snowflake client for querying into pandas DataFrames.

    Reads configuration from explicit arguments or environment variables
    via `SnowflakeClient.from_env()`.
    """

    def __init__(
        self,
        *,
        user: str,
        password: str,
        account: str,
        warehouse: str,
        database: str,
        schema: str,
        role: Optional[str] = None,
        autocommit: bool = True,
        connect_immediately: bool = True,
    ) -> None:
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.role = role
        self.autocommit = autocommit

        self._conn: Optional[sf.SnowflakeConnection] = None
        if connect_immediately:
            self.connect()

    # ---- lifecycle ----
    def connect(self) -> None:
        if self._conn is not None:
            return
        self._conn = sf.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema,
            role=self.role,
            autocommit=self.autocommit,
        )

    def close(self) -> None:
        if self._conn is not None:
            try:
                self._conn.close()
            finally:
                self._conn = None

    def __enter__(self) -> "SnowflakeClient":
        if self._conn is None:
            self.connect()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        self.close()

    # ---- querying ----
    @property
    def connection(self) -> sf.SnowflakeConnection:
        if self._conn is None:
            self.connect()
            assert self._conn is not None
        return self._conn

    def query_to_df(self, sql: str, params: Optional[Sequence[Any]] = None) -> pd.DataFrame:
        """Run a SELECT and return a pandas DataFrame.

        Example placeholders: "SELECT * FROM table WHERE id = %s" with params=(123,)
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params)
            try:
                # Preferred: fast conversion via Snowflake connector
                return cursor.fetch_pandas_all()
            except Exception:
                # Fallback: manual DataFrame construction
                rows = cursor.fetchall()
                columns = [d[0] for d in cursor.description] if cursor.description else []
                return pd.DataFrame.from_records(rows, columns=columns)
        finally:
            cursor.close()

    def execute(self, sql: str, params: Optional[Sequence[Any]] = None) -> None:
        """Execute a non-SELECT statement (CREATE/INSERT/etc.)."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params)
        finally:
            cursor.close()

    def fully_qualified(self, table_name: str) -> str:
        return f"{self.database}.{self.schema}.{table_name}"

    def table_to_df(
        self,
        table_name: str,
        *,
        columns: Optional[Sequence[str]] = None,
        where: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        """Convenience helper to select from a table in the configured database/schema.

        Note: This constructs a simple SQL string. For advanced queries, use `query_to_df`.
        """
        cols_sql = "*" if not columns else ", ".join(columns)
        sql = f"SELECT {cols_sql} FROM {self.fully_qualified(table_name)}"
        if where:
            sql += f" WHERE {where}"
        if order_by:
            sql += f" ORDER BY {order_by}"
        if isinstance(limit, int) and limit > 0:
            sql += f" LIMIT {limit}"
        return self.query_to_df(sql)

    # ---- factories ----
    @classmethod
    def from_env(cls) -> "SnowflakeClient":
        """Load config from environment variables (optionally from a .env file)."""
        module_dir = Path(__file__).resolve().parent
        # Load SQL/.env first (repo-local secrets), then fall back to default search path
        load_dotenv(dotenv_path=module_dir / ".env", override=False)
        load_dotenv(override=False)

        required_keys = [
            "SNOWFLAKE_USER",
            "SNOWFLAKE_PASSWORD",
            "SNOWFLAKE_ACCOUNT",
            "SNOWFLAKE_WAREHOUSE",
            "SNOWFLAKE_DATABASE",
            "SNOWFLAKE_SCHEMA",
        ]
        optional_keys = ["SNOWFLAKE_ROLE"]

        values = {k: os.getenv(k) for k in required_keys + optional_keys}
        missing = [k for k in required_keys if not values.get(k)]
        if missing:
            raise ValueError(
                "Missing required environment variables: " + ", ".join(missing)
            )

        return cls(
            user=str(values["SNOWFLAKE_USER"]),
            password=str(values["SNOWFLAKE_PASSWORD"]),
            account=str(values["SNOWFLAKE_ACCOUNT"]),
            warehouse=str(values["SNOWFLAKE_WAREHOUSE"]),
            database=str(values["SNOWFLAKE_DATABASE"]),
            schema=str(values["SNOWFLAKE_SCHEMA"]),
            role=values.get("SNOWFLAKE_ROLE") or None,
        )


__all__ = ["SnowflakeClient"]


