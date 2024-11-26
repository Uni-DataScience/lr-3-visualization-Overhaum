import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def create_scatter_plot(data):

    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 6))
    scatter_plot = sns.scatterplot(x='x', y='y', data=data, ax=ax, color='#1f77b4', s=80)

    ax.set_title('Scatter Plot of Variables x and y', fontsize=16)
    ax.set_xlabel('Variable x', fontsize=12)
    ax.set_ylabel('Variable y', fontsize=12)

    plt.show()

    return fig

data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

create_scatter_plot(data)
