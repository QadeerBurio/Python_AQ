# class MyClass:
#     def __init__(self):
#         self.__private_variable = 10  # Private variable
#
#     def __private_method(self):  # Private method
#         print("This is a private method")
#
#
# # Create an instance of MyClass
# obj = MyClass()
#
# # Access private variable using name mangling
# print(obj._MyClass__private_variable)  # Output: 10
#
# # Access private method using name mangling
# obj._MyClass__private_method()  # Output: This is a private method
# print(obj.__dir__())
#
#
# class Parent:
#     def __init__(self):
#         self._protected_var = 10  # Protected variable
#
#     def _protected_method(self):  # Protected method
#         print("This is a protected method")
#
# class Child(Parent):
#     def access_protected(self):
#         print(self._protected_var)  # Accessing the protected variable from a subclass
#         self._protected_method()    # Calling the protected method
#
# # Create an instance of the Child class
# child = Child()
#
# # Accessing the protected members via subclass methods
# child.access_protected()  # Output: 10, This is a protected method
#
# # Accessing the protected member directly from outside (not recommended)
# print(child._protected_var)  # Output: 10
#

















class BankAccount:
    def __init__(self, account_holder, cnic, password, initial_balance=0):
        self.account_holder = account_holder  # Public variable
        self.cnic = cnic                      # Public variable
        self.__password = password             # Private variable
        self.__balance = initial_balance        # Private variable

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        """Check the current balance."""
        print(f"Current balance: ${self.__balance}.")

    def authenticate(self, input_cnic, input_password):
        """Authenticate user based on CNIC and password."""
        return self.cnic == input_cnic and self.__password == input_password


class Bank:
    def __init__(self):
        self.accounts = []  # List to store bank accounts

    def create_account(self, account_holder, cnic, password, initial_balance=0):
        """Create a new bank account."""
        new_account = BankAccount(account_holder, cnic, password, initial_balance)
        self.accounts.append(new_account)
        print(f"Account created for {account_holder}.")

    def login(self, cnic, password):
        """Login to the bank account."""
        for account in self.accounts:
            if account.authenticate(cnic, password):
                return account
        print("Authentication failed.")
        return None


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank Management System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            # Create Account
            account_holder = input("Enter account holder name: ")
            cnic = input("Enter CNIC: ")
            password = input("Enter password: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_holder, cnic, password, initial_balance)

        elif choice == '2':
            # Login
            cnic = input("Enter CNIC: ")
            password = input("Enter password: ")
            account = bank.login(cnic, password)

            if account:
                while True:
                    print("\nAccount Menu")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    account_choice = input("Select an option (1-4): ")

                    if account_choice == '1':
                        account.check_balance()
                    elif account_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif account_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif account_choice == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Please try again.")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the main function to start the program
if __name__ == "__main__":
    main()
