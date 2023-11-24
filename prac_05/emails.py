"""
CP1404/CP5632 Practical
Emails

Estimate: 20 minutes
Actual:   15 minutes

"""


def main():
    """ Main function to store user emails and names, and display them."""
    email_names = {}

    user_email = input('Email: ')

    while user_email != "":
        extracted_name = get_name_from_email(user_email)
        response = input(f"Is your name {extracted_name}?(Y/n) ")

        if response.upper() in ["", "Y"]:
            name = extracted_name
        else:
            name = input("Name: ")

        email_names[user_email] = name
        user_email = input('Email: ')

    for user_email, extracted_name in email_names.items():
        print(f"{extracted_name} ({user_email})")


def get_name_from_email(user_email):
    """ Extract the name from the given email address."""
    name = user_email.split("@")[0]
    name_parts = name.split(".")
    full_name = " ".join(name_parts).title()
    return full_name


main()

