"""
CP1404/CP5632 Practical
Hex colours

Estimate: 10 minutes
Actual:   3 minutes

"""

COLOUR_CODES = {"absolute zero": "#0048ba", "amethyst": "#9966cc",
                "apricot": "#fbceb1", "baby pink": "#f4c2c2",
                "bistre": "#3d2b1f", "brick red": "#cb4154",
                "brown1": "#ff4040", "burnt orange": "#cc5500",
                "chartreuse1": "#7fff00", "coquelicot": "#ff3800"}

colour_name = input("Enter colour names: ").lower()
while colour_name != "":
    colour_code = COLOUR_CODES.get(colour_name.lower())
    if colour_code:
        print(f"The code for the colour {colour_name} is {colour_code}.")
    else:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").lower()