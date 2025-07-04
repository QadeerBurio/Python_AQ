# # With Constructors
# class Company:
#     def __init__(self, name, company_id, job):
#         self.name = name
#         self.company_id=company_id
#         self.job=job
#
#     def do_work(self):
#         return "Some Special company in UK "
#
# class Developer(Company):
#     def __init__(self,name,company_id,job, desc, exp):
#         # Using super() to call the parent class's __init__ method
#         super().__init__(name,company_id,job)
#         self.desc = desc
#         self.exp=exp
#
#     def do_work(self):
#         # Extending the parent class method
#         work = super().do_work()  # Calls the parent class's make_sound method
#         return f"{work} (Developer!)"
#
# # Create an instance of Dog
# developer = Developer("AQ","21cs","MERN Developer","Full Stack On site","2years")
#
# # Access methods
# print(developer.name)  # Output: Buddy
# print(developer.desc)  # Output: Golden Retriever
# print(developer.do_work())  # Output: Some generic animal sound (Bark!)
#

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of {self.year} {self.make} {self.model} starts."

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        # Call the parent class (Vehicle) constructor using super()
        super().__init__(make, model, year)
        self.doors = doors

    def start_engine(self):
        # Call the parent class's start_engine method and extend it
        base_message = super().start_engine()
        return f"{base_message} It's a car with {self.doors} doors."

class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_size):
        # Call the parent class (Car) constructor using super()
        super().__init__(make, model, year, doors)
        self.battery_size = battery_size

    def start_engine(self):
        # Call the parent class's start_engine method and modify it
        base_message = super().start_engine()
        return f"{base_message} It's powered by a {self.battery_size}-kWh battery."

# Create instances of Car and ElectricCar
car = Car("Toyota", "Corolla", 2020, 4)
electric_car = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

# Start the engine for both instances
print(car.start_engine())
# Output: The engine of 2020 Toyota Corolla starts. It's a car with 4 doors.

print(electric_car.start_engine())
# Output: The engine of 2023 Tesla Model 3 starts. It's a car with 4 doors. It's powered by a 75-kWh battery.

