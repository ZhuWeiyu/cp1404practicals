import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
number_of_days = 0
OUTPUT_FILE = "output_price.txt"

price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))
out_file = open(OUTPUT_FILE, 'w')
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    number_of_days += 1
    price *= (1 + price_change)
    print("On day {} price is ${:,.2f}".format(number_of_days, price), file=out_file)
out_file.close()