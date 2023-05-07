import csv
from prac_07.guitar import Guitar


def main():
    guitars = []
    get_guitars_from_file(guitars)
    get_new_guitar(guitars)
    display_guitars(guitars)


def get_guitars_from_file(guitars):
    in_file = open("guitars.csv", 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


def display_guitars(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_new_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")

        with open('guitars.csv', 'w') as out_file:
            for guitar in guitars:
                print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)



main()