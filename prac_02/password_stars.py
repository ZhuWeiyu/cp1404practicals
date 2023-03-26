PASSPORT_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = str(input("Enter your password: "))
    while len(password) < PASSPORT_LENGTH:
        print("invalid password")
        password = str(input("Enter your password: "))
    return password


def print_asterisks(password):
    length = len(str(password))
    print("*" * length)


main()