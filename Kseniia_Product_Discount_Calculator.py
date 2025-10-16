# Kseniia, 2025/10/15
# File: Kseniia_Product_Discount_Calculator.py
# Creating a discount calculator
#

# 1. Input

total_original = 0
total_discount_amount = 0
total_final = 0
discount_percentages = []
category_counts = {}
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

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

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

    discount_percentages.append(discount_given)

    # Calculate final price

    discount = price * (discount_given / 100)
    final_price = price - discount

    total_original += price
    total_discount_amount += discount
    total_final += final_price

    details = [
        ("Product", name),
        ("Category", category),
        ("Original Price", f"${price}"),
        ("Discount", f"{discount_given}%"),
        ("Final Price", f"${final_price}")
    ]

    for label, value in details:
        print(f"{label}: {value}")

    print()

    def discount_amount(product):
        return discount

    highest_discount_product = max(products, key=discount_amount)
    average_discount = sum(discount_percentages)/len(discount_percentages)

    if category not in category_counts:
        category_counts[category] = 0
    category_counts[category] += 1

# 3. Output

print("\n=== SUMMARY ===")

print(f"Category_Count: {category_counts}")
print(f"Total_Oritinal: {total_original}")
print(f"Total_Dicount_Amount: {total_discount_amount}")
print(f"Total_Final: {total_final}")
print(f"Highest_Discount_Product: {highest_discount_product['name']}")
print(f"Average_Discount: {average_discount}%")
