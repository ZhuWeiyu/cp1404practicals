from prac_06.guitar import Guitar

def main():

    print("My guitars!")
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1992, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    while True:
        name = input("Name:")
        if name == "":
            break
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name}({year}): ${cost:,.2f}\n")

    length = len(guitars[0].name)
    for guitar in guitars:
        if len(guitar.name) > length:
            length = len(guitar.name)

    print(f"\n... snip ...\n")
    print(f"These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        added = "(vintage)" if guitar.is_vintage() else""
        print(f"Guitar {i}: {guitar.name:>{length}}({guitar.year}), worth $ {guitar.cost:,.2f}  {added} ")


main()