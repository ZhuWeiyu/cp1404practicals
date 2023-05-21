from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0
    print("Lets drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            print("Taxi's available:")
            display_available_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid Taxi Choice")
        elif menu_choice == 'D':
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost ${fare:.2f}")
                total_fare += fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option!")
        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_fare:.2f}")
    display_available_taxis(taxis)


def display_available_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
