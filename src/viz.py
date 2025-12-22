import matplotlib.pyplot as plt
import pandas as pd

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

    fig ,ax = plt.subplots(figsize=(10,4))
    df = df.sort_values("Revenue", ascending=True)
    bars = ax.barh(df["Productname"], df["Revenue"])

    for bar in bars:
        width = bar.get_width()
        ax.text(width + df["Revenue"].max() * 0.01,
                bar.get_y() + bar.get_height()/2,
                f"{int(width):,}",
                va="center", ha="left", fontsize=10)

    ax.set_xlim(0, df["Revenue"].max() * 1.15)

    plt.tight_layout()

    return fig, ax