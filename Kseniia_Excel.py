#
# Kseniia, 2025/10/08
# File: Kseniia_Excel.py
# Calculate sum of column in Excel file.
#

import pandas as pd

# 1. Input

df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process

numeric_sums = df.select_dtypes(include='number').sum()

grand_total = numeric_sums.sum()

# 3. Output

print("Sum per numeric column:")
print(numeric_sums)
print("\nGrand total of all numeric values:", grand_total)

results = numeric_sums.to_frame(name='Sum')
results.loc['Grand Total'] = grand_total

# 4. Output to Excel
results.to_excel('Financial_Sample_Summary.xlsx')

print("✅ Results saved to 'Financial_Sample_Summary.xlsx'")
