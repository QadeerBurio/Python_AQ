# 2. Multiple Inheritance
# A child class inherits from more than one parent class.

class Father:
    def skill1(self):
        print("Father is a painter")

class Mother:
    def skill2(self):
        print("Mother is a singer")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()

# 3. Multilevel Inheritance
# A child class is derived from another child class (a chain of inheritance).

class Grandparent:
    def speak(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def walk(self):
        print("I am Parent")

class Child(Parent):
    def play(self):
        print("I am Child")

c = Child()
c.speak()
c.walk()
c.play()



# 4. Hierarchical Inheritance
# Multiple child classes inherit from the same parent class.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car()
b = Bike()
c.start()
b.start()



# 5. Hybrid Inheritance
# A combination of multiple and multilevel inheritance.

class A:
    def feature1(self):
        print("Feature 1 from A")

class B(A):
    def feature2(self):
        print("Feature 2 from B")

class C:
    def feature3(self):
        print("Feature 3 from C")

class D(B, C):
    def feature4(self):
        print("Feature 4 from D")

d = D()
d.feature1()
d.feature3()
d.feature4()