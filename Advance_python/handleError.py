# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Division by zero is not allowed")
#     return a / b
#
# try:
#     print(divide(10, 0))
# except ZeroDivisionError as e:
#     print("Error:", e)
# finally:
#     print("This always runs!")



class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds in the account!")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

try:
    acc = BankAccount("AQ", 1000)
    acc.withdraw(1500)  # trying to withdraw more than balance
except InsufficientFundsError as e:
    print("Error:", e)
finally:
    print("Transaction ended.")
