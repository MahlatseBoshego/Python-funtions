
price = float(input("Enter your price: R"))
discount_percent = float(input("Enter discount (%): "))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * discount_percent / 100
        return price - discount
    else:
        return price



final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied: {discount_percent}%")
print(f"Final price: R{final_price:.2f}")



   

























