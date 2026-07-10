import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def row_count(file):
    df = pd.read_csv(file, index_col = 0)
    row_sums = df.sum(axis = 1)
    print(row_sums)
    
    # allow tiny floating ploint / rounding tolerance
    assert (abs(row_sums - 1) < 1e-3).all(), "Some rows don't sum to 1"
    
    return df

def transition_heatmap(df):
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.replace(0, 1e-6), norm=LogNorm(), cmap='viridis')
    plt.title('1-Year Rating Transition Matrix')
    plt.xlabel('To Rating')
    plt.ylabel('From Rating')
    plt.tight_layout()
    plt.show()

