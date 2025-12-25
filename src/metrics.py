import pandas as pd
import matplotlib.pyplot as plt
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

def number_over_bar(df, target1, target2) -> plt:
    fig ,ax = plt.subplots(figsize=(12,4))
    bars = df[f"[{target1}]",f"[{target2}]"]
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height +3,
                str(int(height)), ha="center", va="bottom", color="Black", fontweight="bold")
    return