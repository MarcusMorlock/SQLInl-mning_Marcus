import pandas as pd
from sqlalchemy import create_engine, text

# Wrapper‑klass som kör SQL‑queries och returnerar DataFrames till notebooken.

from .io_utiles import (connect_to_sql
                        
                        )
class SqlReport:
    def __init__(self):
        self.engine = connect_to_sql()

    def query_df(self, sql: str)-> pd.DataFrame:
        """
        Take a Sql formated query and return a DataFrame with the result.
        """
        with self.engine.connect() as conn:
            return pd.read_sql(text(sql), conn)