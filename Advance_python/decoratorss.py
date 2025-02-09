import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " mil sec")
        return result
    return wrapper  # <-- Fixed this line

@time_it
def calc_sqrt(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

array = range(1, 100000)

out_square = calc_sqrt(array)
out_cube = calc_cube(array)




#  Built-in Decorators
# Python provides built-in decorators such as:
#
# @staticmethod and @classmethod
#

# class MathUtils:
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#     @classmethod
#     def description(cls):
#         return f"This is a {cls.__name__} class."
#
# print(MathUtils.add(5, 7))
# print(MathUtils.description())


# @property Decorator (for getters and setters)
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if not value:
#             raise ValueError("Name cannot be empty.")
#         self._name = value
#
# p = Person("Alice")
# print(p.name)
# p.name = "Bob"
# print(p.name)



# Decorators with parameters


# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet():
#     print("Hello!")
#
# greet()



# Timing

# import time
#
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start:.2f} seconds")
#         return result
#     return wrapper
#
# @timing_decorator
# def slow_function():
#     time.sleep(2)
#     print("Function finished")
#
# slow_function()



# authentication
# def requires_authentication(func):
#     def wrapper(user):
#         if user != "admin":
#             print("Access denied!")
#         else:
#             return func(user)
#     return wrapper
#
# @requires_authentication
# def dashboard(user):
#     print(f"Welcome {user} to the dashboard!")
#
# dashboard("guest")
# dashboard("admin")




# Summary of Key Points:
# Function decorators: Modify or enhance functions.
# Arguments in decorators: Handle *args and **kwargs for flexibility.
# Built-in decorators: @staticmethod, @classmethod, @property.
# Chaining decorators: Apply multiple decorators to a single function.
# Class-based decorators: Use __call__ for decorator logic.
# Preserve function metadata: Use functools.wraps.
# Real-world usage: Flask routing, logging, authentication, timing.