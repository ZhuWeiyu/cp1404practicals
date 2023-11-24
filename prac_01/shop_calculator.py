total = 0
DISCOUNT_RATE = 0.9
DISCOUNT_PRICE = 100

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number.")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    # solution: price_of_item = float(input(f"Enter price of item {i+1} : $"))
    total += price_of_item

if total > DISCOUNT_PRICE:
    total *= DISCOUNT_RATE
print(f"Total price for {number_of_items} items is ${total:.2f}")