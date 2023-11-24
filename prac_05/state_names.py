"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting

Estimate: 5 minutes
Actual:   5 minutes

"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# print all the states and their abbreviations
for key, value in CODE_TO_NAME.items():
    print("{:3} is {}".format(key, value))

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()