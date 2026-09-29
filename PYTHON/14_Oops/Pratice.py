# Q1. Employee

# Create an abstract class Employee.
# Create an abstract method work().
# Create a child class Developer.
# Implement work() in Developer.
# Create an object and call work().


# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass

# class Developer(Employee):
#     def work(self):
#         print("the work will start")

# obj = Developer()                     #Call the child fumction
# obj.work()       



# Q2. Animal

# Create abstract class Animal.
# Add abstract method sound().
# Create Dog and Cat classes.
# Implement sound() differently in both.
# Create objects and call the method.


# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("dog barks in night") 

# class Cat(Animal):
#     def sound(self):
#         print("cat meows in day")              

# obj = Dog()                        #call the child function
# obj.sound()

# t = Cat()                          #call the child function
# t.sound()



# Level 2 — Abstract + Concrete Methods

# Q3. Payment
# Create an abstract class Payment with:

# Abstract method: pay(amount)
# Concrete method: receipt()

# Create:

# CreditCard
# UPI
# Cash

# Each child class should implement pay() differently.

# from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass                        #abstract method

#     def receipt(self):
#         print("Got the reciept")    #concrete method

# class Credit(Payment):
#     def pay(self,amount):
#         print("pay the", amount, "using credit card")       

# class UPI(Payment):
#     def pay(self,amount):
#         print("pay the",amount, "using UPI")

# class Cash(Payment):
#     def pay(self,amount):
#         print("pay the",amount, "using cash")

# ob1 = Credit()
# ob1.pay(2000)
# ob1.receipt()

# ob2 = UPI()
# ob2.pay(1599)
# ob2.receipt()

# ob3 = Cash()
# ob3.pay(1999)
# ob3.receipt()



# Q4. Vehicle
# Create an abstract class Vehicle with:

# start() → abstract
# stop() → concrete, prints "Vehicle stopped"

# Create Car and Bike classes and implement start()

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print("vehicle should start")       #abstract method

#     def stop(self):
#         print("Vehicle Stopped")             #concrete method

# class Car(Vehicle):
#     def start(self):
#         print("start the car")

# class Bike(Vehicle):
#     def start(self):
#         print("start the bike")


# car = Car()
# car.start()

# bike = Bike()
# bike.start()
