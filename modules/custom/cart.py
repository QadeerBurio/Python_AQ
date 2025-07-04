# cart.py

from product import Product

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the cart")
        self.cart.append(product)

    def remove_product(self, product_name):
        self.cart = [product for product in self.cart if product.name != product_name]

    def calculate_total(self):
        return sum(product.calculate_total_price() for product in self.cart)

    def display_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            for product in self.cart:
                print(product)

    def clear_cart(self):
        self.cart.clear()

    def __str__(self):
        return f"ShoppingCart with {len(self.cart)} items"
