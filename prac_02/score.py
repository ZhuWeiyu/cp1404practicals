import random

LOWEST_SCORES = 0
HIGHEST_SCORES = 100
EXCELLENT_SCORES = 90
PASS_SCORES = 50


def main():
    score = get_valid_score()
    score_level = determine_score_level(score)
    print(score_level)
    score = random.randint(0, 100)
    score_level = determine_score_level(score)
    print(f"Your random score is {score} and your random score level is {score_level}")


def get_valid_score():
    score = float(input("Enter score:"))
    while LOWEST_SCORES>score or score > HIGHEST_SCORES:
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


main()