# Level 3 — Practical

# Q5. Bank Account
# Create an abstract class BankAccount:

# deposit(amount) → concrete
# withdraw(amount) → abstract
# show_balance() → concrete

# Create SavingsAccount and CurrentAccount.

# Each child should have its own implementation of withdraw().

# from abc import ABC,abstractmethod

# class BankAccount(ABC):
#     @abstractmethod 
#     def withdraw(self):
#         pass

#     def amount(self):
#         print("total amount")

#     def show_balance(self):
#         print("show_balance")    

# class SavingsAccount(BankAccount):
#     def withdraw(self):
#         print("this is savings account")

# class currentAccount(BankAccount):
#     def withdraw(self):
#         print("this is current account")      

# obj = SavingsAccount()
# obj.withdraw()

# obj1 = currentAccount()
# obj1.withdraw()


# # This is also way to write the code



# from abc import ABC, abstractmethod

# class BankAccount(ABC):

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     def deposit(self, amount):
#         print("Deposited:", amount)

#     def show_balance(self):
#         print("Showing balance")


# class SavingsAccount(BankAccount):

#     def withdraw(self, amount):
#         print("Withdraw from savings account:", amount)


# class CurrentAccount(BankAccount):

#     def withdraw(self, amount):
#         print("Withdraw from current account:", amount)


# obj = SavingsAccount()
# obj.withdraw(500)
# obj.deposit(2000)
# obj.show_balance()

# obj1 = CurrentAccount()
# obj1.withdraw(1000)
# obj1.deposit(3000)
# obj1.show_balance()