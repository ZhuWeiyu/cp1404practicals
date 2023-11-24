"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_RATE = 0.1
HIGH_RATE = 0.15
VALUE_OF_SALES = 1000


sales = float(input("Enter sales:$ "))
while sales >= 0:
    if sales >= VALUE_OF_SALES:
        user_bonus = sales * LOW_RATE
    else:
        user_bonus = sales * HIGH_RATE
    print(f"Bonus: {user_bonus:.2f} ")
    sales = float(input("Enter sales:$ "))
else:
    print("Invalid")