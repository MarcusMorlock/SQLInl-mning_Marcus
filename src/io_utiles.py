import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def connect_to_sql():
    user = "SA"
    password = quote_plus("Xardas519!")
    server = "localhost:1433"
    database = "AdventureWorks2025"
    driver = quote_plus("ODBC Driver 17 for SQL Server")

    connection_string = (
        f"mssql+pyodbc://{user}:{password}@{server}/{database}"
        f"?driver={driver}&Encrypt=yes&TrustServerCertificate=yes"
    )

    engine = create_engine(connection_string)



    try:
        with engine.connect():
            print("anslutning till sql server lyckades")
    except Exception as e:
        print("kunde inte ansluta", e)

    return engine

