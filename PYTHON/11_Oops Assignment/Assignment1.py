
# 1) Banking System — Inheritance + Method Overriding
# Create a Banking System with:
# BankAccount as the parent class with:

# account_number
# holder_name
# balance
# deposit()
# withdraw()

# Create child classes:
# SavingsAccount
# CurrentAccount

# Each account should have different withdrawal rules.
# Override the withdraw() method in child classes.
# Create multiple account objects and perform transactions.


# class BankAccount:

#     def __init__(self, account_number, holder_name, balance):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#         print("Balance:", self.balance)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#             print("Balance:", self.balance)
#         else:
#             print("Insufficient balance")


# class SavingsAccount(BankAccount):

#     def withdraw(self, amount):
#         if self.balance - amount >= 1000:
#             self.balance -= amount
#             print("Savings Account")
#             print("Withdrawn:", amount)
#             print("Balance:", self.balance)
#         else:
#             print("Withdrawal failed")
#             print("Minimum balance of ₹1000 must be maintained")


# class CurrentAccount(BankAccount):

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Current Account")
#             print("Withdrawn:", amount)
#             print("Balance:", self.balance)
#         else:
#             print("Insufficient balance")


# # Creating objects

# s1 = SavingsAccount("S101", "Yaswanth", 10000)
# c1 = CurrentAccount("C101", "Rahul", 5000)


# # Transactions

# s1.deposit(2000)
# s1.withdraw(5000)

# print()

# c1.deposit(1000)
# c1.withdraw(5500)



# 2.Create an Employee Payroll System using multilevel inheritance:

# Person
#    ↓
# Employee
#    ↓
# Manager

# Requirements:

# Person → name, age
# Employee → employee ID, basic salary
# Manager → bonus, team size
# Calculate the final salary.
# Override a method such as calculate_salary() in Manager.
# Create objects for both employees and managers.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):

    def __init__(self, name, age, employee_id, basic_salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class Manager(Employee):

    def __init__(self, name, age, employee_id, basic_salary, bonus, team_size):
        super().__init__(name, age, employee_id, basic_salary)
        self.bonus = bonus
        self.team_size = team_size

    # Method Overriding
    def calculate_salary(self):
        return self.basic_salary + self.bonus


# Employee object
e1 = Employee("Yaswanth", 23, "E101", 30000)

# Manager object
m1 = Manager("Rahul", 30, "M101", 50000, 15000, 8)


# Display Employee details
print("Employee Name:", e1.name)
print("Employee Age:", e1.age)
print("Employee ID:", e1.employee_id)
print("Employee Salary:", e1.calculate_salary())

print()

# Display Manager details
print("Manager Name:", m1.name)
print("Manager Age:", m1.age)
print("Manager ID:", m1.employee_id)
print("Team Size:", m1.team_size)
print("Manager Salary:", m1.calculate_salary())



