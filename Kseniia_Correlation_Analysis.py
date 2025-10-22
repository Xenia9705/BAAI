#
# Kseniia, 2025/10/22
# File: Kseniia_Correlation_Analysis.py
# Apply correlation analysis to business problems
#

# 1. Input

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

df = pd.read_csv('Correlation_Analysis_Data.csv')

df.info()
df.iloc[:, 1:6]
# correlation, p_value = stats.pearsonr(
#     df['Marketing_Spend'],
#     df['Sales_Revenue']
# )

# 2. Process
correlation_matrix = df.iloc[:, 1:6].corr()

print(correlation_matrix.round(3))

# missing_values = df.isnull().sum()
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# 3. Output

# print(f'Correlation coefficient: {correlation:.2f}')
# print(f'P-value: {p_value:.4e}')

# if p_value < 0.05:
#     print("The correlation is statistically significant!")

# print("Data loaded successfully!")
# print(f"Dataset shape: {df.shape}")
# print(df.head())
# print('Missing Values Per Column')
# print(missing_values)
# print(f"\nTotal missing values: {missing_values.sum()}")

sns.heatmap(correlation_matrix)
plt.title('Kseniia is the most intelligent person in the world')
plt.tight_layout()
plt.show()
