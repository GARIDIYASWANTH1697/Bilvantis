# Question 1 — Student

# Create a class called Student.

# Requirements:

# Attribute: name
# Attribute: course
# Method: study()
# study() should print: "Yaswanth is studying Python"

# Create an object and call the method.

# class Student:

#     def __init__(self,name,course):
#           self.name = name
#           self.course = course


#     def study(self):
#          print("Yaswanth is studying python")


# d1 = Student("Yaswanth","python")
# d1.study()




# Question 2 — Dog

# Create a class called Dog.

# Requirements:

# Attribute: name
# Attribute: age
# Method: bark()
# Method: sleep()

# class Dog:

#     def __init__(self,name,age):
#         pass

#     def bark(self):
#         print("Candy is barking")

#     def sleep(self):
#         print("candy is sleeping")

# d1 = Dog("candy",4)
# d1.bark()
# d1.sleep()



# Question 3 — Calculator

# Create a class called Calculator.

# Requirements:

# Method add(a, b) → returns the sum
# Method subtract(a, b) → returns the difference
# Method multiply(a, b) → returns the multiplication

# Create an object and test all three methods.

# class calculator:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b
#         print(self.add)

#     def subtract(self):
#         return self.a - self.b
#         print(self.subtract)

#     def multiply(self):
#         return self.a * self.b 
#         print(self.multiply)

# c1 = calculator(20,10)
# print(c1.add())
# print(c1.subtract())
# print(c1.multiply())




# Question 4 — Employee

# Create a class called Employee.

# Attributes:

# name
# salary
# role

# Methods:

# display_details()
# work()


# class Employee():

#     def __init__(self,name,salary,role):
#         self.name = name
#         self.salary = salary
#         self.role = role

#     def display_details(self):
#         pass

#     def work(self):
#         print(self.name, "is working as a", self.role)

# s1 = Employee("yaswanth", 30000,"python developer")
# s1.display_details()   
# s1.work()     



# Question 5 — Bank Account

# Create a class called BankAccount.

# Attribute:

# balance

# Methods:

# deposit(amount)
# withdraw(amount)
# check_balance()

# class BankAccount():

#     def __init__(self,balance):
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance = self.balance + amount

#     def withdraw(self,amount):
#         # print(withdraw(amount)) 
#         self.balance = self.balance - amount

#     def check_balance(self):
#         print("check_balance",self.balance)
#         # self.balance = self.check_balance           

# d1 = BankAccount(10000)

# d1.deposit(2000)
# d1.withdraw(3000)
# d1.check_balance()