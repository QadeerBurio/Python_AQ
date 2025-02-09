# Creating a set with curly braces
# my_set = {1, 2, 3, 4, 4, 5}
# print(my_set)  # Output: {1, 2, 3, 4, 5}
#
# # Creating a set using the set() function
# another_set = set([1, 2, 3, 2, 1])
# print(another_set)  # Output: {1, 2, 3} (duplicates are removed)
#
#
# # Adding an element
# my_set.add(6)
# print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
#
# # Removing an element
# another_set.remove(3)
# print(another_set)  # Output: {1, 2}
#
# another_set.discard(1)
# print(another_set)


# Operations
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# # Union
# union_set = set1 | set2
# print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}
#
# # Intersection
# intersection_set = set1 & set2
# print("Intersection:", intersection_set)  # Output: {3, 4}
#
# # Difference
# difference_set = set1 - set2
# print("Difference:", difference_set)  # Output: {1, 2}
#
# # Symmetric Difference  except same elements
# symmetric_difference_set = set1 ^ set2
# print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 5, 6}


# Iteration

# my_set = {1, 2, 3, 4, 5}
# for item in my_set:
#     print(item)


# Comprehension
# squared_set = {x**2 for x in range(5)}
# print(squared_set)  # Output: {0, 1, 4, 9, 16}

# my_set = {1, 2, 3}
# print(len(my_set))  # Output: 3
#
# # Checking if one set is a subset of another
# small_set = {1, 2}
# print(small_set.issubset(my_set))  # Output: True


# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b


