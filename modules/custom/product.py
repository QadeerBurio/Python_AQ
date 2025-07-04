# product.py

class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity} = ${self.calculate_total_price()}"
