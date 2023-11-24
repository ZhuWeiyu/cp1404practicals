SCORE_MINIMUM = 0
SCORE_MIDDLE = 50
SCORE_HIGH = 90
SCORE_MAXIMUM = 100

MENU = "(G)et a valid score\n(P)rint result \n(S)how stars\n(Q)uit"


def main():
    """Executes the main program logic, display the menu"""
    print(MENU)
    score = float(input("Please enter your score first: "))
    score = get_valid_score(score)
    choice = input("<<< Your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Please enter your score: "))
            score = get_valid_score(score)
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid.")
        print(MENU)
        choice = input("<<< Your choice: ").upper()
    else:
        print("Farewell.")


def get_valid_score(score):
    """Ensure the input score is within a valid range and prompts the user to re-enter if it's not"""
    while score <= SCORE_MINIMUM or score >= SCORE_MAXIMUM:
        print("Invalid.")
        score = float(input("Please enter your score: "))
    return score


def determine_score(score):
    """Determine the score level based on the given score and returns the result."""
    if SCORE_MINIMUM < score < SCORE_MIDDLE:
        level = "Bad"
    elif score < SCORE_HIGH:
        level = "Pass"
    elif score <= SCORE_MAXIMUM:
        level = "Excellent"
    else:
        level = "Invalid"
    return level


def show_stars(score):
    """Display as many stars as the given score"""
    print('*' * int(score))


main()