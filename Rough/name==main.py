# We use name==main




def add(a, b):
    try:
        return a + b
    except TypeError as e:
        print(f"Error in add(): {e}")
        return None


def subtract(a, b):
    try:
        return a - b
    except TypeError as e:
        print(f"Error in subtract(): {e}")
        return None


def multiply(a, b):
    try:
        return a * b
    except TypeError as e:
        print(f"Error in multiply(): {e}")
        return None


def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    except (TypeError, ValueError) as e:
        print(f"Error in divide(): {e}")
        return None


def get_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None


if __name__ == "__main__":
    print("Welcome to the calculator program!")

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            print("Exiting the program.")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please try again.")
            continue

        a, b = get_numbers()
        if a is None or b is None:
            print("Failed to get valid numbers. Restarting operation...")
            continue

        if choice == 1:
            result = add(a, b)
        elif choice == 2:
            result = subtract(a, b)
        elif choice == 3:
            result = multiply(a, b)
        elif choice == 4:
            result = divide(a, b)

        if result is not None:
            print(f"The result is: {result}")
        else:
            print("An error occurred during the calculation.")
