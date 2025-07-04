# Simple Lambda Function:

# add=lambda x,y:x*y*2
# print(add(5,5))

# Use Map In Lambda:

# # List of numbers
# numbers = [1, 2, 3, 4, 5]
#
# # Lambda function to square each number
# squared = list(map(lambda x: x ** 3, numbers))
# print(squared)  # Output: [1, 4, 9, 16, 25]




# The filter() function constructs an iterator from elements of an iterable for which a function returns true. Lambda functions are often used with filter() to filter out elements that meet a certain condition.


# List of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # Lambda function to filter out even numbers
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# odd=list(filter(lambda x: x%2!=0, numbers))
#
# print(odd)  # Output: [2, 4, 6, 8, 10]
# print(evens)  # Output: [1, 3, 5, 7, 9]



# The reduce() function from the functools module applies a rolling computation to sequential pairs of values in a list. Lambda functions are often used with reduce() for operations like summing or multiplying elements.


# from functools import reduce
#
# # List of numbers
# numbers = [1, 2, 3, 4, 5]
#
# # Lambda function to compute the product of all elements
# product = reduce(lambda x, y: x * y, numbers)
#
# print(product)  # Output: 120




# is and == use:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Check if a and b refer to the same object in memory
print(a == b)  # Output: False

# Check if a and c refer to the same object in memory
print(a is c)  # Output: True



a = None

# Correct way to check for None
if a is None:
    print("a is None")

# It is also possible to use `==` to check for None, but `is` is the recommended approach
if a == None:  # Not recommended, but will work
    print("a is None")
