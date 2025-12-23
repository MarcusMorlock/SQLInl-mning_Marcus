import matplotlib.pyplot as plt
import pandas as pd
from src.metrics import(
    year_month_combined,
)
# Innehåller alla matplotlib‑visualiseringar. Tar emot färdigprocessade DataFrames från metrics.

def viz_products_per_category(df: pd.DataFrame) -> plt:

    fig ,ax = plt.subplots(figsize=(8,6))

    products = ax.bar(df["Productname"], df["amount"])
    
   
    for bar in products:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height +3,
                str(int(height)), ha="center", va="bottom", color="Black", fontweight="bold")
        
    ax.set_ylim(0, max(df["amount"]) + 10)        
    ax.set_title("Amount of products", fontsize=12 , fontweight="bold")
    ax.set_xlabel("Product", fontsize=12)
    ax.set_ylabel("Amount of Products", fontsize=12)  

    plt.tight_layout()


    return fig, ax

def viz_total_sell_per_category(df: pd.DataFrame) -> plt:
    
    fig ,ax = plt.subplots(figsize=(12,4))
    df = df.sort_values("Revenue", ascending=True)
    bars = ax.barh(df["Productname"], df["Revenue"])

    for bar in bars:
        width = bar.get_width()
        ax.text(width + df["Revenue"].max() * 0.01,
                bar.get_y() + bar.get_height()/2,
                f"{int(width):,}",
                va="center", ha="left", fontsize=10)

    ax.set_xlim(0, df["Revenue"].max() * 1.15)
    ax.ticklabel_format(style="plain", axis="x")
    plt.tight_layout()

    return fig, ax

def viz_sell_per_month(df: pd.DataFrame) -> plt:
    df = year_month_combined(df)
    fig ,ax = plt.subplots(figsize=(10,6))
    X = df["YearMonth"]
    Y = df["Revenue"]
    ax.plot(X, Y, marker="o", linestyle="-", linewidth="3")

    ax.ticklabel_format(style="plain", axis="y")
    ax.set_title("Monthly Revenue from Mid-2022 to 2024", fontsize=16)
    ax.set_xlabel("Year-Month", fontsize="15")
    ax.set_ylabel("Revenue", fontsize="15")
    ax.grid(True, axis="both")

    plt.tight_layout()

    return fig, ax

