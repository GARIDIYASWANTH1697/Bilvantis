#1) What is a class in Python? Create a Student class with name and age.

# answer : class is a blueprint to create the object

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj = Student("Yash",23)

print(obj.name)
print(obj.age)


#2) What is an object? Create two objects from the Student class.

# answer : object means instance of the class

obj = Student("kiran",21)
obj1  = Student("Murali",24)

print(obj.name)
print(obj.age)

print(obj1.name)
print(obj1.age)


# 3)What is the purpose of __init__()?

# answer : __init__ is used to intilized the objects

# 4)Write a class Employee with:

# name
# salary
# display_details() method

class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        pass    


# 5)What does self mean in Python?

# self is a reference to the current instance of the class


# 6)Create a Car class with brand and model. Create 2 objects and print their details.

class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

s1 = Car("toyota","s11")   

s2 = Car("suzuki","s44")

print(s1.brand)
print(s1.model)

print(s2.brand)
print(s2.model)



# 7)Create a BankAccount class with:

# account_holder
# balance
# deposit()
# withdraw()

class BankAccount():
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        pass

    def withdraw(self,amount):
        pass

        
# 8)Create an Employee class with a private variable __salary. Create a method to display the salary.    

class Employee():
    def __init__(self,salary):
        self.__salary = salary

    def display(self):
        pass    



# 9)Create a Student class with a class variable college = "ABC College". Create 3 students and display their college.    

class Student():

    college = "ABC College"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

obj = Student("swamy",20000)
obj1 = Student("kiran",30000)
obj2 = Student("mahesh",40000)

print(obj.college)
print(obj1.college)
print(obj2.college)