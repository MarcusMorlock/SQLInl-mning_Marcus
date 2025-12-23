import pandas as pd

# Innehåller funktioner för databeräkningar, aggregeringar och transformationer (ingen visualisering).

def product_per_category(df: pd.DataFrame) -> pd.DataFrame:
    return df

def sell_product_per_category(df: pd.DataFrame) -> pd.DataFrame:
    return df

def year_month_combined(df: pd.DataFrame) -> pd.DataFrame:
    df["YearMonth"] = pd.to_datetime(df["OrderYear"].astype(str) + "-" + df["OrderMonth"].astype(str))
    df.drop(columns=["OrderYear", "OrderMonth"], inplace=True)
    df = df[["YearMonth", "Revenue"]]
    return df