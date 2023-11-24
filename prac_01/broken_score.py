"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# FIXED:
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50
MIN_SCORE = 0

score = float(input("Enter score: "))
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid")
elif score >= EXCELLENT_SCORE:
    print("Excellent")
elif score >= PASS_SCORE:
    print("Passable")
else:
    print("Bad")

