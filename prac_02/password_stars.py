MIN_LENGTH = 8


def main():
    """Execute the main program logic."""
    password = get_valid_password()
    display_stars(password)


def get_valid_password():
    """ Prompt user for a password and validate its length. """
    user_password = input("Enter password: ")
    while len(user_password) < MIN_LENGTH:
        print("Invalid password, please type at least 8 characters.")
        user_password = input("Enter password: ")
    return user_password


def display_stars(user_password):
    """Display the given password as a series of asterisks."""
    print("*" * len(user_password))


main()
