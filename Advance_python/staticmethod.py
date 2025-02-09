# class MathOperations:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#
# # Calling static methods without creating an instance
# result_add = MathOperations.add(5, 3)  # Returns 8
# result_multiply = MathOperations.multiply(5, 3)  # Returns 15
#
# print("Addition:", result_add)  # Output: Addition: 8
# print("Multiplication:", result_multiply)  # Output: Multiplication: 15
#

# Class Method
class Person:
    population = 0  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
        Person.population += 1  # Modify class attribute

    @classmethod
    def get_population(cls):
        return f"Total population is: {cls.population}"


# Creating instances
person1 = Person("Alice")
person2 = Person("Bob")

# Accessing the class method
print(Person.get_population())  # Output: Total population is: 2
print(person1.get_population())  # Output: Total population is: 2




# Class Method as alternative constructor


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Calculate age based on the current year (assuming current year is 2024)
        age = 2024 - birth_year
        # Return an instance of the class
        return cls(name, age)

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

# Creating an instance using the regular constructor
person1 = Person("Alice", 30)

# Creating an instance using the alternative constructor (from_birth_year)
person2 = Person.from_birth_year("Bob", 1995)

print(person1.display())  # Output: Name: Alice, Age: 30
print(person2.display())  # Output: Name: Bob, Age: 29
