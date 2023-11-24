import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate quick picks"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid.")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick(NUMBERS_PER_LINE)
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick(n):
    """Generate a quick pick with n numbers"""
    quick_pick = []
    for i in range(n):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


main()