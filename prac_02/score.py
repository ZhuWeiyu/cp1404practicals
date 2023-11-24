import random


SCORE_MINIMUM = 0
SCORE_MIDDLE = 50
SCORE_HIGH = 90
SCORE_MAXIMUM = 100


def main():
    """Execute the main program """
    score = generate_random_score()
    print(f"Random score: {score}")
    print(determine_score(score))


def determine_score(score):
    """Determine the score level based on the given score"""
    if SCORE_MINIMUM < score < SCORE_MIDDLE:
        level = "bad"
    elif score < SCORE_HIGH:
        level = "pass"
    elif score < SCORE_MAXIMUM:
        level = "excellent"
    else:
        level = "Invalid"
    return level


def generate_random_score():
    """Generate a random score between minimum and maximum."""
    return random.randint(SCORE_MINIMUM, SCORE_MAXIMUM)


main()