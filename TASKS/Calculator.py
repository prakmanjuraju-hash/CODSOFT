def calculator():
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print(f"Result: {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1 * num2}")
    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    while True:
        calculator()
        again = input("\nDo you want to calculate again? (y/n): ").lower()
        if again != "y":
            print("Exiting Calculator. Goodbye!")
            break
