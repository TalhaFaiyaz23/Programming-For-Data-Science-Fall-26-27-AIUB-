# Problem Statement : Create a list of dictionaries representing four products.Each dictionary must contain a product name, price, and quantity.Use a loop to calculate the total cost. Write a function named apply_discount(total) that applies a 10% discount when the total is at least 2,000. Otherwise, return the original total.

# Solve : 

cart = [
    {"name": "Wireless Mouse", "price": 800, "quantity": 1},
    {"name": "Keyboard", "price": 1200, "quantity": 1},
    {"name": "USB Cable", "price": 250, "quantity": 2},
    {"name": "Mousepad", "price": 150, "quantity": 1}
]

# Function to apply a 10% discount when total is at least 2,000
def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    return total

# Calculate total cost using a loop
subtotal = 0
for item in cart:
    subtotal += item["price"] * item["quantity"]

final_total = apply_discount(subtotal)

print(f"Subtotal: {subtotal}")
print(f"Final Total (after discount check): {final_total}")