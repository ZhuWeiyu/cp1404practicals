"""
function main()
    get number_of_quickpicks
    quickpicks = []
    for i in range(number_of_quickpicks):
        quickpick = generate_a_quickpick()
        quickpicks.append(quickpick)

    for quickpick in quickpicks:
        format_print_quickpick(quickpick)

function generate_a_quickpick()
    numbers = []
    while len(numbers) < LENGTH_OF_QUICKPICK:
        get random number
        if number not in numbers:
            numbers.append(number)

    return sorted(numbers)

function format_print_quickpick(quickpick)
    for number in quickpick:
        print(f"{number:2d}", end=" ")
    print()
"""

import random

MINIMUM = 1
MAXIMUM = 45
LENGTH_OF_QUICKPICK = 6


def main():
    number_of_quickpicks = int(input("How many quick picks? "))
    quickpicks = []
    for i in range(number_of_quickpicks):
        quickpick = generate_a_quickpick()
        quickpicks.append(quickpick)

    for quickpick in quickpicks:
        format_print_quickpick(quickpick)


def test():
    quickpick = generate_a_quickpick()
    print(quickpick)
    format_print_quickpick(quickpick)


def generate_a_quickpick():
    numbers = []
    while len(numbers) < LENGTH_OF_QUICKPICK:
        number = random.randint(MINIMUM, MAXIMUM + 1)
        if number not in numbers:
            numbers.append(number)

    return sorted(numbers)


def format_print_quickpick(quickpick):
    for number in quickpick:
        print(f"{number:2d}", end=" ")
    print()


main()
