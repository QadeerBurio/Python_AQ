import math
import random
import datetime


def factorial(n):
    """Return the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)


def random_matrix(rows, cols, min_val=0, max_val=10):
    """Generate a random matrix with the specified dimensions."""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def days_between(date1, date2):
    """Return the number of days between two dates."""
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def complex_operation(a, b):
    """Perform a complex operation combining various built-in functions."""
    return math.sqrt(a ** 2 + b ** 2) + math.log(math.fabs(a - b) + 1)


def main():
    print("Choose an operation:")
    print("1. Factorial")
    print("2. Random Matrix")
    print("3. Days Between Dates")
    print("4. Complex Operation")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        n = int(input("Enter a number for factorial calculation: "))
        try:
            result = factorial(n)
            print(f"Factorial of {n}: {result}")
        except ValueError as e:
            print(e)

    elif choice == '2':
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        min_val = int(input("Enter minimum value for matrix elements: "))
        max_val = int(input("Enter maximum value for matrix elements: "))
        matrix = random_matrix(rows, cols, min_val, max_val)
        print("Random matrix:")
        for row in matrix:
            print(row)

    elif choice == '3':
        date1 = input("Enter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")
        try:
            days = days_between(date1, date2)
            print(f"Days between {date1} and {date2}: {days}")
        except ValueError as e:
            print(e)

    elif choice == '4':
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        result = complex_operation(a, b)
        print(f"Result of complex operation with a={a} and b={b}: {result}")

    else:
        print("Invalid choice. Please select a number between 1 and 4.")


# Entry point for the module
if __name__ == "__main__":
    main()
