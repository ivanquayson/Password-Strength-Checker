import re


def checkPassword(password):
    print("Checking password...", password)

    # Check for length of password
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters long.")
        return False

    # Check for uppercase, lowercase, numbers, and special characters
    if not re.search("[A-Z]", password):
        print("Password should contain at least one uppercase letter")
        return False
    if not re.search("[a-z]", password):
        print("Password should contain at least one lowercase letter")
        return False
    if not re.search("[0-9]", password):
        print("Password needs at least one number")
        return False
    special_chars = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    if not any(char in special_chars for char in password):
        print("Password should contain at least one special character")
        return False

    print("Password is strong!")
    return True


def main():
    password = input("Enter your password: ")
    if checkPassword(password):
        print("Good job!")
    else:
        print("Password is too weak. Please try again.")


if __name__ == "__main__":
    main()
