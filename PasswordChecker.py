"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import string
MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    else:

        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
    for char in password:
        if char in string.ascii_lowercase:
            count_lower += 1
        elif char in string.ascii_uppercase:
            count_upper += 1
        elif char in string.digits:
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        else:
            return False


    if count_lower > 0 and count_upper > 0 and count_digit > 0:
        if SPECIAL_CHARS_REQUIRED == True:
            if count_special > 0:
                return True
            else:
                return False
        return True
    else:
        return False



main()