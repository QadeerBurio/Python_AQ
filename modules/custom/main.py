# main.py

from product import Product
from cart import ShoppingCart
from store import Store


def main():
    store = Store()
    cart = ShoppingCart()

    # Initial products
    store.add_product_to_inventory(Product("Laptop", 999.99))
    store.add_product_to_inventory(Product("Smartphone", 499.99))
    store.add_product_to_inventory(Product("Headphones", 99.99))

    print("Welcome to the Online Store!")
    while True:
        print("\n1. View Store Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Remove Product from Cart")
        print("5. Checkout")
        print("6. Add Product Manually")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable Products:")
            store.list_products()

        elif choice == '2':
            product_name = input("Enter the product name to add to cart: ")
            product = store.find_product_by_name(product_name)
            if product:
                quantity = int(input(f"Enter quantity for {product_name}: "))
                product.update_quantity(quantity)
                cart.add_product(product)
                print(f"Added {quantity} of {product_name} to your cart.")
            else:
                print("Product not found in store.")

        elif choice == '3':
            print("\nYour Cart:")
            cart.display_cart()

        elif choice == '4':
            product_name = input("Enter the product name to remove from cart: ")
            cart.remove_product(product_name)
            print(f"Removed {product_name} from your cart.")

        elif choice == '5':
            print("\nYour Cart:")
            cart.display_cart()
            print(f"Total: ${cart.calculate_total():.2f}")
            proceed = input("Do you want to proceed to checkout? (yes/no): ")
            if proceed.lower() == 'yes':
                print("Thank you for your purchase!")
                cart.clear_cart()

        elif choice == '6':
            store.add_product_manually()

        elif choice == '7':
            print("Exiting the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
