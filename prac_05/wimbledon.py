FILENAME = "wimbledon.csv"


def main():
    datas = read_csv_file(FILENAME)
    champions, countries = get_champions(datas)
    display_data(champions, countries)


def read_csv_file(FILENAME):
    datas = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            datas.append(parts)
    return datas


def get_champions(datas):
    champions = {}
    countries = set()
    for data in datas:
        countries.add(data[1])
        try:
            champions[data[2]] += 1
        except KeyError:
            champions[data[2]] = 1
    return champions, countries


def display_data(champions, countries):
    print("Wimbledon Champions:")
    for name, champion in champions.items():
        print(name, champion)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()