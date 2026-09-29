# Defination of Encapsulation:
# Encapsulation is the process of bundling data(attributes) and methods that operate on that data inside a single class


# Example:

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         self.balance = self.balance - amount

#     def check_balance(self):
#         print("Balance:", self.balance)


# account = BankAccount(10000)

# account.deposit(2000)
# account.withdraw(3000)
# account.check_balance()


# Question 1 — Student

# Create a class called Student.

# Requirements:
# Create an attribute name
# Create an attribute marks
# Create a method display_details()
# The method should display the student's name and marks.


# class Student():

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks 

#     def display_details(self):
#         print("name",self.name)
#         print("marks",self.marks)    

# pupil = Student("Yaswanth",85)
# pupil.display_details()




# Question 2 — Private Attribute

# Now let's practice the data protection/control-access part of encapsulation.

# Create a class called BankAccount.

# Requirements:
# Create a private attribute __balance
# Create a method deposit(amount) to add money
# Create a method check_balance() to display the balance
# Create an object with initial balance 10000

# class BankAccount:

#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance = self.__balance + amount

#     def check_balance(self):
#         print("Balance",self.__balance)    

# Balance = BankAccount(10000)
# Balance.deposit(2000)
# Balance.check_balance()



# 3)protected Attribute

# class BankAccount:

#     def __init__(self,balance):
#         self._balance = balance

#     def deposit(self,amount):
#         self._balance = self._balance + amount

#     def check_balance(self):
#         print("Balance",self._balance)    

# Balance = BankAccount(10000)
# Balance.deposit(2000)
# Balance.check_balance()



# 4) Inheritance of protected

# class BankAccount:

#     def __init__(self,balance):
#         self._balance = balance

#     def deposit(self,amount):
#         self._balance = self._balance + amount

#     def check_balance(self):
#         print("Balance",self._balance)    

# class SavingsAccount(BankAccount):

#     def show_balance(self):
#         print(self._balance)        

# Balance = BankAccount(10000)
# Balance.deposit(2000)
# Balance.check_balance()

# s1 = SavingsAccount(15000)
# s1.show_balance()