"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BASIC_SALES = 0
UPPER_SALES = 1000
sales = float(input("Enter sales: $"))
while sales >= BASIC_SALES:
    if sales < UPPER_SALES:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Bonus: ${int(bonus)}")
    sales = float(input("Enter sales: $"))