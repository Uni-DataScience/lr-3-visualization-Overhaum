import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_1d(data):

    plt.figure(figsize=(8, 6))
    plt.plot(data, color='blue', label='1D Data')
    plt.title('1D Line Plot', fontsize=16)
    plt.xlabel('Index', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_2d(x, y):

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='green', label='2D Data', alpha=0.7)
    plt.title('2D Scatter Plot', fontsize=16)
    plt.xlabel('X Values', fontsize=12)
    plt.ylabel('Y Values', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_3d(x, y, z):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=z, cmap='viridis', label='3D Data')
    ax.set_title('3D Scatter Plot', fontsize=16)
    ax.set_xlabel('X Values', fontsize=12)
    ax.set_ylabel('Y Values', fontsize=12)
    ax.set_zlabel('Z Values', fontsize=12)
    fig.colorbar(scatter, ax=ax, label='Color (Z)')
    plt.legend()
    plt.show()

x = np.linspace(0, 10, 100)  # Дані для осі X
y = np.sin(x)                # Дані для осі Y
z = np.cos(x)                # Дані для осі Z

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
