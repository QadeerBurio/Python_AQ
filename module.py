
# Modules
#
# import math
#
# # Use the sqrt function from the math module
# result = math.sqrt(16)
# print(result)  # Output: 4.0


# # import custom module
# import sets
#
# # Call functions from sets
# print(sets.greet("Sami"))  # Output: Hello, Sami!
# print(sets.add(5, 3))      # Output: 8

#
# from sets import greet
# print(greet("Sami"))  # Output: Hello, Sami!
#
# import sets as mm
#
# print(mm.greet("Sami"))  # Output: Hello, Sami!
#
# from sets import *
#
# print(greet("Sami"))  # Output: Hello, Sami!
# print(add(5, 3))      # Output: 8
#
# import sys
#
# # Add the directory to the Python path
# sys.path.append(r'D:\Data Science\Python')
#
# # Optional: Print the current Python path to verify
# print(sys.path)

#
# import json
#
# # Python dictionary
# data = {
#     "name": "Sami",
#     "age": 21,
#     "university": "Mehran University",
#     "courses": ["Math", "Physics", "Computer Science"]
# }
#
# # Convert Python dictionary to JSON string
# json_data = json.dumps(data, indent=4)  # The indent parameter is optional and is used for pretty-printing
# print(json_data)
#
#
# # convert json format into python object
#
# import json
#
# # JSON string
# json_data = '''
# {
#     "name": "Sami",
#     "age": 21,
#     "university": "Mehran University",
#     "courses": ["Math", "Physics", "Computer Science"]
# }
# '''
#
# # Convert JSON string to Python dictionary
# data = json.loads(json_data)
#
# print(data)
# print(data["name"])  # Accessing data from the dictionary
#
#


#
# # Writing Python Objects to a JSON File
# import json
#
# # Python dictionary
# data = {
#     "name": "Sami",
#     "age": 21,
#     "university": "Mehran University",
#     "courses": ["Math", "Physics", "Computer Science"]
# }
#
# # Write JSON data to a file
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)  # The indent parameter is optional and is used for pretty-printing
#
# # Reading JSON Data from a File
# import json
#
# # Read JSON data from a file
# with open('dataa.json', 'r') as json_file:
#     data = json.load(json_file)
#
# print(data)




# We will write two programs
# 1: To create address book and write some records into it
# 2: Read this address book



# 1
# convert
# import json
#
# # python dictionary
#
# data = {
#     "name": "Sami",
#     "age": 21,
#     "university": "Mehran University",
#     "courses": ["Math", "Physics", "Computer Science"]
# }
#
# js=json.dumps(data)
# print(js)

#
# # Write
#
# import json
#
# # Python dictionary
# book = {
#     "name": "AQ",
#     "age": 21,
#     "university": "Mehran University",
#     "courses": ["Maths", "Python", "Computer Science"]
# }
#
# # Write JSON data to a file
# with open('data.txt', 'w') as json_file:
#     json.dump(book, json_file, indent=4)  # The indent parameter is optional and is used for pretty-printing
#
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)
#
# print(type(data), data)







