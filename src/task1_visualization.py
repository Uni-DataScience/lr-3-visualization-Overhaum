import matplotlib.pyplot as plt
import numpy as np
import collections

def plot_distribution(data):

    counter = collections.Counter(data)
    categories = list(counter.keys())
    frequencies = list(counter.values())

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(categories, frequencies, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    ax.set_xlabel('Категорія', fontsize=12)
    ax.set_ylabel('Частота', fontsize=12)
    ax.set_title('Розподіл категоричних даних', fontsize=14)
    ax.bar_label(bars, fmt='%d', padding=3, fontsize=10)

    plt.show()

    return fig

data = np.random.choice(['A', 'B', 'C'], size=100)

plot_distribution(data)
