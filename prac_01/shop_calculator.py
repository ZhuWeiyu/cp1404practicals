DISCOUNT = 0.1
MINIMUM_NUMBERS = 0
DISCOUNT_PRICE = 100
TOTAL_PRICE = 0

numbers = int(input("Number of item: "))
while numbers < MINIMUM_NUMBERS:
    print("Invalid number of items!")
    numbers = int(input("Number of item: "))
for i in range(numbers):
    price = float(input("Price of item: "))
    TOTAL_PRICE += price

if TOTAL_PRICE > DISCOUNT_PRICE:
    final_price = TOTAL_PRICE * (1-DISCOUNT)

else:
    final_price = TOTAL_PRICE

print(f"Total price for {numbers} items is ${final_price}")