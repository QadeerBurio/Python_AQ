# class Employee:
#     """Base class for all employees in the company."""
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id
#
#     def work(self):
#         return f"{self.name} is working."
#
#     def __str__(self):
#         return f"Employee(Name: {self.name}, ID: {self.employee_id})"
#
#
# class Developer(Employee):
#     """Subclass representing a developer."""
#     def __init__(self, name, employee_id, programming_language):
#         super().__init__(name, employee_id)
#         self.programming_language = programming_language
#
#     def work(self):
#         return f"{self.name} is coding in {self.programming_language}."
#
#     def __str__(self):
#         return f"Developer(Name: {self.name}, ID: {self.employee_id}, Language: {self.programming_language})"
#
#
# class Manager(Employee):
#     """Subclass representing a manager."""
#     def __init__(self, name, employee_id, team_size):
#         super().__init__(name, employee_id)
#         self.team_size = team_size
#
#     def work(self):
#         return f"{self.name} is managing a team of {self.team_size} employees."
#
#     def __str__(self):
#         return f"Manager(Name: {self.name}, ID: {self.employee_id}, Team Size: {self.team_size})"
#
#
# # Function to demonstrate polymorphism
# def show_employee_work(employee):
#     print(employee.work())
#     print(f"Is instance of Employee: {isinstance(employee, Employee)}")
#     print(f"Is instance of Developer: {isinstance(employee, Developer)}")
#     print(f"Is instance of Manager: {isinstance(employee, Manager)}")
#     print()
#
# # Creating employee objects
# dev1 = Developer("Alice", 101, "Python")
# dev2 = Developer("Bob", 102, "JavaScript")
# mgr1 = Manager("Charlie", 201, 5)
#
# # Showing work output and type checks
# show_employee_work(dev1)
# show_employee_work(dev2)
# show_employee_work(mgr1)



class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())












# GeekForGeek



# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

print(dir(Employee))