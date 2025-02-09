class Vehicle:
    def general_usage(self):
        print("General Usage: Transportation")

class Car(Vehicle):
    def __init__(self):
        print("Here Is Car!")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific usage: Commuting to work, vacations with family")

class Bike(Vehicle):
    def __init__(self):
        print("Here Is Bike!")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific usage: Racing, road trips")


c = Car()
c.general_usage()
c.specific_usage()

b = Bike()
b.general_usage()
b.specific_usage()



# Isinstance

class Vehicle:
    def general_usage(self):
        print("General Usage: Transportation")

class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific usage: Commuting to work, vacations with family")

class Bike(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific usage: Racing, road trips")

# Creating instances
car = Car()
bike = Bike()

# Using isinstance() to check types
print(isinstance(car, Car))        # Output: True
print(isinstance(car, Vehicle))     # Output: True
print(isinstance(bike, Bike))       # Output: True
print(isinstance(bike, Vehicle))    # Output: True
print(isinstance(bike, Car))        # Output: False

# Checking for multiple types
print(isinstance(car, (Car, Bike)))  # Output: True
print(isinstance(bike, (Car, Vehicle)))  # Output: True




# issubclass

class Parent:
    pass

class Child(Parent):
    pass

# Check if Child is a subclass of Parent
print(issubclass(Child, Parent))  # Output: True

# Check if Parent is a subclass of Child
print(issubclass(Parent, Child))  # Output: False

# Check if Child is a subclass of itself
print(issubclass(Child, Child))  # Output: True

