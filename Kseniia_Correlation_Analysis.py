#
# Kseniia, 2025/10/22
# File: Kseniia_Correlation_Analysis.py
# Apply correlation analysis to business problems
#

# 1. Input

import pandas as pd

df = pd.read_csv('Simple_Data.csv')


# 2. Process
missing_values = df.isnull().sum()

# 3. Output

print("Data loaded successfully!")
print(f"Dataset shape: {df.shape}")
print(df.head())
print('Missing Values Per Column')
print(missing_values)
print(f"\nTotal missing values: {missing_values.sum()}")
