import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def perform_eda(df):

    print("Описова статистика:")
    descriptive_stats = df.describe().T
    descriptive_stats['mode'] = df.mode().iloc[0]  # Додаємо моду
    print(descriptive_stats)
    print("\n")

    print("Box plot для виявлення викидів:")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, palette='Set2')
    plt.title('Box Plot для виявлення викидів', fontsize=14)
    plt.show()

    print("Матриця кореляцій:")
    correlation_matrix = df.corr()
    print(correlation_matrix)
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title('Теплова карта кореляції', fontsize=14)
    plt.show()

    print("Пояснення результатів:")
    print("- Описова статистика дає огляд центральних тенденцій і розподілу кожної змінної.")
    print("- Box plot ідентифікує можливі викиди в наборі даних.")
    print("- Кореляційний аналіз показує ступінь зв'язку між змінними.")

df = pd.DataFrame({
    'A': np.random.rand(50),          # Рівномірний розподіл [0, 1]
    'B': np.random.rand(50) * 10,    # Рівномірний розподіл [0, 10]
    'C': np.random.rand(50) * 100    # Рівномірний розподіл [0, 100]
})

perform_eda(df)
