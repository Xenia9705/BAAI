#
# Kseniia, 2025/10/15
# File: Kseniia_Product_Discount_Calculator.py
# Short description of the task
#
# Initialize tracking variables

# 1. Input

total_original = 0
total_discount_amount = 0
total_final = 0

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

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

# 2. Process

for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # Determine discount
    if category == "Electronics":
        if price >= 1000:
            discount_given = 20
        elif price >= 500:
            discount_given = 15
        else:
            discount_given = 10

    elif category == "Clothing":
        if price >= 100:
            discount_given = 25
        else:
            discount_given = 15

    elif category == "Books":
        discount_given = 10

    # Calculate final price
    discount = price * (discount_given / 100)
    final_price = price - discount

    total_original += price
    total_discount_amount += discount
    total_final += final_price

    print(f"Product: {name} | Category: {category} | Original Price: ${price} | Discount: {discount_given}% | Final Price: ${final_price}")

# TODO: Update totals
# Print summary
print("\n=== SUMMARY ===")
# TODO: Print total statistics
