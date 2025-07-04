# dir()

my_list = [1, 2, 3]
print(dir(my_list))

# Help

 # Using help() on a built-in function
help(len)

# Using help() on a user-defined class
class MyClass:
    """This is a simple class."""
    def my_method(self):
        """This method does something."""
        pass

help(MyClass)

# Output will include the docstring of the class and its method:
# Help on class MyClass in module __main__:
# class MyClass(builtins.object)
#  |  This is a simple class.
#  |
#  |  Methods defined here:
#  |
#  |  my_method(self)
#  |      This method does something.


# __dic__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person1 = Person("Alice", 30)

# Access the __dict__ attribute
print(person1.__dict__)
# Output: {'name': 'Alice', 'age': 30}

