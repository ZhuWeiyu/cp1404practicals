import random
LOWEST_LIMIT = 0
HIGHEST_LIMIT = 100
EXCELLENT_SCORES = 90
PASS_SCORES = 50


def main():
    score = float(input("Enter score:"))
    if score < LOWEST_LIMIT or score > HIGHEST_LIMIT:
        print("invalid score")
    else:
        print(user_score(score))

    random_score = random.randint(LOWEST_LIMIT, HIGHEST_LIMIT + 1)
    print(f"\nRandom score {random_score}")
    print(f"Examination level；{user_score(random_score)}")


def user_score(score):
    if score >= PASS_SCORES:
        return "Passable"
    elif score >= EXCELLENT_SCORES:
        return "Excellent"
    elif score < PASS_SCORES:
        return "Bad"



main()