COLOR_NAME = {"Amaranth": "#e52b50", "Aqua": "#00ffff",
              "Aureolin": "#fdee00", "Apricot": "#fbceb1",
              "Azure1": "#f0ffff", "Bittersweet": "#fe6f5e",
              "Black": "#000000", "Blond": "#faf0be",
              "Blue1": "#0000ff", "Blue2": "#0000ee"}
choice = input("Enter a color name: ").title()
while choice != "":
    print("The code for \"{}\" is {}".format(choice, COLOR_NAME.get(choice)))
    choice = input("Enter a color name: ").title()