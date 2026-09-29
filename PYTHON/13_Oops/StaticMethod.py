# The important point is:

# Instance method → uses self
# Class method → uses cls
# Static method → uses neither self nor cls


#  Syntex

# class ClassName:

#     @staticmethod
#     def method_name():
#         # code


# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b


# result = Calculator.add(10, 20)

# print(result)



# class Student:

#     @staticmethod
#     def college_rules():
#         print("Students must maintain 75% attendance")


# Student.college_rules()



# class BankAccount:

#     bank_name = "ABC Bank"

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     # 1. Instance Method
#     def show_balance(self):
#         print("Name:", self.name)
#         print("Balance:", self.balance)

#     # 2. Class Method
#     @classmethod
#     def show_bank(cls):
#         print("Bank:", cls.bank_name)

#     # 3. Static Method
#     @staticmethod
#     def interest_rate():
#         print("Interest rate is 7%")


# account = BankAccount("Yaswanth", 10000)

# account.show_balance()
# BankAccount.show_bank()
# BankAccount.interest_rate()





# class Employee:

#     company = "ABC"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self):
#         print(self.name, self.salary)

#     @classmethod
#     def show_company(cls):
#         print(cls.company)

#     @staticmethod
#     def welcome():
#         print("Welcome to ABC company")







