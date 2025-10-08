#
# Kseniia, 2025/10/08
# File: Kseniia_Excel.py
# Calculate sum of column in Excel file.
#

import pandas as pd

# 1. Input

df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process

sum = df.select_dtypes(include='number').sum()
# numeric_sum = df.sum(numeric_only=True)

# 3. Output
# print("Sum of numeric columns:")
# print(numeric_sum)

print(f'Sum{sum}')
