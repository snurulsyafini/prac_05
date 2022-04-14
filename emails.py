def main():
    """Create empty dictionary to store emails to name"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = get_name_from_email(user_email)
        confirm_input = input(f"Is your name {user_name}? (Y/n) ")
        if confirm_input.upper() != "Y" and confirm_input != "":
            user_name = input("Name: ")
        email_to_name[user_email] = user_name
        user_email = input("Email: ")

    for user_email, user_name in email_to_name.items():
        print(f"{user_name} ({user_email})")


def get_name_from_email(user_email):
    """Get name from email"""
    special_word = user_email.split("@")[0]
    parts = special_word.split(".")
    user_name = " ".join(parts).title()
    return user_name


if __name__ == '__main__':
    main()
