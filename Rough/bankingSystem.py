class InsufficientFundsError(Exception):
    """Exception raised when an account has insufficient funds."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Attempted to withdraw {amount}, but only {balance} is available.")


class ExceedsWithdrawalLimitError(Exception):
    """Exception raised when the withdrawal amount exceeds the limit."""

    def __init__(self, limit, amount):
        self.limit = limit
        self.amount = amount
        super().__init__(f"Attempted to withdraw {amount}, but the limit is {limit}.")


class UnauthorizedAccessError(Exception):
    """Exception raised when a user tries to access an unauthorized account."""

    def __init__(self, user, account):
        self.user = user
        self.account = account
        super().__init__(f"User {user} is not authorized to access account {account}.")


class BankAccount:
    def __init__(self, owner, balance=0, withdrawal_limit=1000):
        self.owner = owner
        self.balance = balance
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount, user):
        if user != self.owner:
            raise UnauthorizedAccessError(user, self.owner)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        if amount > self.withdrawal_limit:
            raise ExceedsWithdrawalLimitError(self.withdrawal_limit, amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_balance(self):
        return self.balance


# Function to display options and process user input
def banking_system():
    owner = input("Enter the account owner's name: ")
    balance = float(input("Enter the initial balance: "))
    withdrawal_limit = float(input("Enter the withdrawal limit: "))
    account = BankAccount(owner, balance, withdrawal_limit)

    while True:
        print("\nOptions:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            new_balance = account.deposit(amount)
            print(f"Deposited {amount}. New balance: {new_balance}")

        elif choice == "2":
            user = input("Enter your name: ")
            amount = float(input("Enter amount to withdraw: "))
            try:
                new_balance = account.withdraw(amount, user)
                print(f"Withdrew {amount}. New balance: {new_balance}")
            except Exception as e:
                print(e)

        elif choice == "3":
            print(f"Current balance: {account.check_balance()}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose a valid one.")


# Run the banking system
if __name__ == "__main__":
    banking_system()
