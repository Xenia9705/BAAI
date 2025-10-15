#
# Kseniia, 2025/10/15
# File: Kseniia_Product_Discount_Calculator.py
# Short description of the task
#
# Initialize tracking variables
total_original = 0
total_discount_amount = 0
total_final = 0
print("=== PRODUCT DISCOUNT CALCULATOR ===\n")
# Process each product
products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 45, "category": "Clothing"},
    {"name": "Phone", "price": 800, "category": "Electronics"},
    {"name": "Shoes", "price": 120, "category": "Clothing"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Jacket", "price": 95, "category": "Clothing"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Headphones", "price": 150, "category": "Electronics"}
]
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]
if category == "Electronics":
    if price >= 1000:
        discount = 20
    elif price >= 500:
        discount = 15
    else:
        discount = 10
elif category == "Clothing":
    if price >= 100:
        discount = 25
    else:
        discount = 15
elif category == "Books":
    discount = 10
# TODO: Calculate final price
discount = price * (discount_percent / 100)
final_price = price - discount
total_original += price
total_discount_amount += discount
total_final += final_price
# TODO: Print product details
# TODO: Update totals
# Print summary
print("\n=== SUMMARY ===")
# TODO: Print total statistics
