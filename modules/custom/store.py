# store.py

from product import Product

class Store:
    def __init__(self):
        self.inventory = []

    def add_product_to_inventory(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to inventory")
        self.inventory.append(product)

    def list_products(self):
        if not self.inventory:
            print("No products available in the store.")
        else:
            for product in self.inventory:
                print(product)

    def find_product_by_name(self, name):
        for product in self.inventory:
            if product.name == name:
                return product
        return None

    def add_product_manually(self):
        try:
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the product quantity: "))
            product = Product(name, price, quantity)
            self.add_product_to_inventory(product)
            print(f"Product '{name}' added successfully!")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def __str__(self):
        return f"Store with {len(self.inventory)} products"
