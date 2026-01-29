import random
import string


def generate_password(length):
    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter desired password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    password = generate_password(length)
    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
