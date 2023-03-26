MENU = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit"""
LOWEST_SCORES = 0
HIGHEST_SCORES = 100
EXCELLENT_SCORES = 90
PASS_SCORES = 50


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_level(score)
            print(f"Your score level result is {result}")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thanks for you playing. See you next time.")


def get_valid_score():
    score = int(input("Enter score: "))
    while LOWEST_SCORES > score or score > HIGHEST_SCORES:
        print("invalid score")
        score = float(input("Enter score:"))
    return score


def determine_score_level(score):
    if score >= EXCELLENT_SCORES:
        score_level = "excellent"
    elif score >= PASS_SCORES:
        score_level = "pass"
    else:
        score_level = "bad"
    return score_level


def print_asterisks(score):
    print("*" * score)


main()