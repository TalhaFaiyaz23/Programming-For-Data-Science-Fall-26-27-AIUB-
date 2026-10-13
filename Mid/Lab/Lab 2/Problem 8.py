# Problem Statement : Calculate each product’s line total using price * quantity. Calculate the total inventory value and identify the product with the highest line total.


#Solve :

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total_inventory_value = 0
highest_line_total = -1
top_product = ""

# Calculate each product's line total and track inventory stats
for product in products:
    line_total = product["price"] * product["quantity"]
    total_inventory_value += line_total
    
    print(f"Product: {product['name']} | Line Total: {line_total}")
    
    # Identify the product with the highest line total
    if line_total > highest_line_total:
        highest_line_total = line_total
        top_product = product["name"]

print("\n--- Inventory Summary ---")
print(f"Total Inventory Value: {total_inventory_value}")
print(f"Product with Highest Line Total: {top_product} ({highest_line_total})")