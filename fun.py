# Define expense lists
# aq_exp_list = [250, 300, 500, 600]
# haji_exp_list = [300, 200, 400, 900]
#
# # Calculate and print AQ total expenses
# total = 0
# for item in aq_exp_list:
#     total += item
# print("AQ Total Expense:", total)
#
# # Calculate and print Haji total expenses
# total = 0
# for item in haji_exp_list:
#     total += item
# print("Haji Total Expense:", total)

# Reduce line of code use functions

# def calculate_total_expense(expense_list, name):
#     total = sum(expense_list)
#     print(f"{name} Total Expense: {total}")
#
# # Define expense lists
# aq_exp_list = [250, 300, 500, 600]
# haji_exp_list = [300, 200, 400, 900]
#
# # Calculate total expenses
# calculate_total_expense(aq_exp_list, "AQ")
# calculate_total_expense(haji_exp_list, "Haji")

# # sum of two numbers
#
# def add(a, b):
#     """Add two numbers and return the result."""
#     return a + b
#
# n = add(3, 5)
# print(n)
#
# # Print the docstring of the 'add' function
# print(add.__doc__)


#Global or local variable

# total= 10  # Global variable
#
# def add(a,b):
#     total=a+b  # Local variable
#     print(total)
#     return total
#
# n=add(7,5)
# print(total)

# *args: For non-keyword variable-length arguments.
# def sum_all(*numbers):
#     """Return the sum of all numbers provided."""
#     return sum(numbers)
#
# print(sum_all(1, 2, 3))  # Output: 6
# print(sum_all(4, 5, 6, 7))  # Output: 22

# **kwargs: For keyword variable-length arguments.

# def describe_person(**details):
#     """Print out details about a person."""
#     for key, value in details.items():
#         print(f"{key}: {value}")
#
# describe_person(name="Sami", age=21, location="Pakistan")


# Creating a dictionary

# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
#
# # Alternatively, using the dict() function
# another_dict = dict(name="Bob", age=30, city="Los Angeles")
#
# # Accessing value using square brackets
# print(my_dict["name"])  # Output: Alice

# # Accessing value using get()
# print(my_dict.get("age"))  # Output: 25
# # Using get() with a default value
# print(my_dict.get("gender", "Not specified",))  # Output: Not specified
#
#
#
# # Adding a new key-value pair
# my_dict["email"] = "alice@example.com"
#
# # Updating an existing key-value pair
# my_dict["age"] = 26
#
# print(my_dict)
# # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
#
#
# # Adding a new key-value pair
# another_dict["email"] = "alice@example.com"
#
# # Updating an existing key-value pair
# another_dict["age"] = 26
#
# print(another_dict)
#
#
#
#
# # Iterating over keys
# for key in my_dict:
#     print(key, my_dict[key])
#
# # Iterating over values
# for value in my_dict.values():
#     print(value)
#
# # Iterating over key-value pairs
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")




# 2nd dictionary


# Example: Storing contact information


# contacts = {
#     "Alice": "alice@example.com",
#     "Bob": "bob@example.com",
#     "Charlie": "charlie@example.com"
# }
#
# # Adding a new contact
# contacts["David"] = "david@example.com"
#
# # Updating an existing contact
# contacts["Alice"] = "alice_new@example.com"
#
# # Removing a contact
# del contacts["Charlie"]
#
# # Displaying contacts
# for name, email in contacts.items():
#     print(f"Name: {name}, Email: {email}")





# Tuples

# # Function returning multiple values
# def get_person_info():
#     return ("Alice", 30, "New York")
#
# name, age, city = get_person_info()
# print(f"Name: {name}, \n Age: {age}, \n City: {city}")
#
# # Using tuples as dictionary keys
# locations = {("New York", "NY"): "USA", ("London", "LDN"): "UK"}
# print(locations[("New York", "NY")])  # Output: USA


# 2nd code:

countries=["UK","USA","SPAIN","CANADA"]

temp=list(countries)
temp.append("RUSSIA")
temp.pop(4)
temp[2]="Russia"
countries=tuple(temp)
print(countries)



