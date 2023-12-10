from prac_06.guitar import Guitar


def main():
    """Main function to manage the guitar collection."""
    guitars = read_guitars_from_file("guitars.csv")

    print("My guitars!")
    new_guitars = get_new_guitars_from_user()
    guitars.extend(new_guitars)

    write_guitars_to_file("guitars.csv", guitars)
    print("\nNew guitars saved to file.")

    guitars.sort()
    print("\nThese are my guitars:")
    display_guitars(guitars)


def read_guitars_from_file(filename):
    """Read guitars from a given file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """ Display guitars in a formatted output."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitars_from_user():
    """Get guitar details from the user and return a list of new Guitar objects."""
    new_guitars = []
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        new_guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.\n")
        name = input("Name: ")

    return new_guitars


def write_guitars_to_file(filename, guitars):
    """Write guitars to a given file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
