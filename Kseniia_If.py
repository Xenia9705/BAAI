#
# Kseniia, 2025/10/15
# File: Kseniia_If.py
# Short description of the task
#

# 1. Input

order_value = [120, 450, 80, 300, 650]
total_revenue = 0

for order in order_value:
    total_revenue += order
    print(f"Processing order: $ {order}")

print(f"\nTotal Revenue: $ {total_revenue}")
