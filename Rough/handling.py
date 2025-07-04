# code 1: Basic Error Handling with try and except

# try:
#     a = int(input("Enter the Number: "))
#     print(f"Multiplication table of {a} is")
#
#     for i in range(1, 11):
#         print(f"{a} X {i} = {a * i}")
#
# except ValueError:
#     print("Invalid Input: Please enter a valid number.")
#
# else:
#     print("Some important line of code:")



# # code 2: Handling Multiple Exceptions
# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Invalid input! Please enter a number.")


# Code 3: try and multiple except
# try:
#     num = int(input("Enter the number: "))
#     a=[6,4]
#     print(a[num])
# except ValueError:
#     print("The number entered is not an integer")
# except IndexError:
#     print("Index Error!")

# code 4: except with else

# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Invalid input! Please enter a number.")
# else:
#     print("Result:", result)  # This runs only if no exception occurred


# code 5: Finally keyword:

# try:
#     file = open('data.txt', 'r')
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Done")
#     file.close()  # This will run whether or not an exception was raised

# code 6: finally in def

# def funct1():
#     try:
#         i=[1,2,4,6,7]
#         a=int(input("Enter the number: "))
#         print(i[a])
#         return 1
#     except:
#         print("Some error occured!")
#         return 0
#     finally:
#         print("I am always excuted!")
#
# x=funct1()
# print(x)


# code 7: Custom error using raise

# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be 18 or older.")
#     return "Access granted."
#
# try:
#     print(check_age(15))
# except ValueError as e:
#     print("Error:", e)

# code 8: custom exception error with class
#
# class CustomError(Exception):
#     """Custom exception class."""
#     pass
#
# def do_something(value):
#     if value < 0:
#         raise CustomError("Negative value not allowed!")
#
# try:
#     do_something(-5)
# except CustomError as e:
#     print("Caught a custom exception:", e)


# # more complex:
# def handle_input(value):
#     try:
#         number = int(value)
#         result = 10 / number
#     except ValueError:
#         print("Error: Invalid input. Please enter a number.")
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")
#     else:
#         print(f"Result: {result}")
#     finally:
#         print("Input handling complete.")
#
# # Example usage
# handle_input("abc")  # Raises ValueError
# handle_input("0")    # Raises ZeroDivisionError
# handle_input("5")    # Executes successfully



class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def set_age(age):
    try:
        if age < 0:
            raise InvalidAgeError("Age cannot be negative.")
        print(f"Age set to: {age}")
    except InvalidAgeError as e:
        print(f"Error: {e}")

# Example usage
set_age(int(input("Enter Your Age: ")))  # Raises custom InvalidAgeError






