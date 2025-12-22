import matplotlib.pyplot as plt
import pandas as pd

# Innehåller alla matplotlib‑visualiseringar. Tar emot färdigprocessade DataFrames från metrics.

def viz_products_per_category(df: pd.DataFrame) -> plt:

    fig ,ax = plt.subplots(figsize=(8,6))

    products = ax.bar(df["Productname"], df["amount"])
    
    ax.set_ylim(0, max(df["amount"]) + 10)
    for bar in products:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height +3,
                str(int(height)), ha="center", va="bottom", color="Black", fontweight="bold")
        
    ax.set_title("Amount of products", fontsize=12 , fontweight="bold")
    ax.set_xlabel("Product", fontsize=12)
    ax.set_ylabel("Amount of Products", fontsize=12)  

    plt.tight_layout()


    return fig, ax