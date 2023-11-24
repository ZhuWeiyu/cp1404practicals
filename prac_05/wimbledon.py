"""
CP1404/CP5632 Practical
Wimbledon

Estimate: 30 minutes
Actual:   24 minutes

"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Main function that runs the program. """
    data = get_data(FILENAME)
    champions = get_champions(data)
    countries = list(get_countries(data))
    countries.sort()

    print("Wimbledon Champions: ")
    for champions, count in champions.items():
        print(f"{champions} {count}")
    print()
    print(f"These are {len(countries)} countries have won Wimbledon: ")
    print(",".join(countries))


def get_data(filename):
    """Reads a CSV file and returns its data as a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            row = line.strip().split(',')
            data.append(row)
    return data


def get_champions(data):
    """Counts the number of championships won by each player."""
    champions = {}
    for row in data:
        champion = row[CHAMPION_INDEX]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """Extracts the unique set of countries from the CSV data."""
    countries = set()
    for row in data:
        countries.add(row[COUNTRY_INDEX])
    return countries


main()
