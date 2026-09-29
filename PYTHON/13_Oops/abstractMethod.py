# from abc import ABC, abstractmethod

# class PaymentGateway(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass

# class CreditCardPayment(PaymentGateway):
#     def process_payment(self, amount):
#         print(f"Processing credit card payment of {amount}")

# class PayPalPayment(PaymentGateway):
#     def process_payment(self, amount):
#         print(f"Processing PayPal payment of {amount}")




# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass   # abstract method

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# # Calling abstract method via subclass
# dog = Dog()
# print(dog.sound())   # Output: Bark

# cat = Cat()
# print(cat.sound())   # Output: Meow


# 1. Animal
# Create an abstract class Animal.

# Requirements:

# Create an abstract method sound().
# Create child classes Dog and Cat.
# Dog.sound() → "Dog barks"
# Cat.sound() → "Cat meows"
# Create objects and call sound().

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("cat meows")

# dog = Dog()
# dog.sound()

# cat = Cat()
# cat.sound()


# 2. Shape
# Create an abstract class Shape.

# Requirements:

# Abstract method: area()
# Create Circle and Rectangle.
# Implement area() differently in each child class.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self):
#         print("This is area of Circle")

# class Rectangle(Shape):
#     def area(self):
#         print("This is area of Rectangle")  

# circle = Circle()
# circle.area()

# rectangle = Rectangle()
# rectangle.area()


# 6. Payment System

# Create an abstract class Payment.

# Requirements:

# Instance variable amount
# Abstract method pay()
# Create:
# CreditCard
# UPI
# Cash
# Each class should implement pay() differently.


# from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
        
# class CreditCard(Payment):
#     def pay(self,amount):
#         self.amount = amount
#         print("paying by Credit card")


# class UPI(Payment):
#     def pay(self,amount):
#         self.amount = amount
#         print("paying by UPI")

# class Cash(Payment):
#     def pay(self,amount):
#         self.amount = amount
#         print("paying by cash")     

# cash = CreditCard()
# cash.pay(10000)

# upi = UPI()
# upi.pay(5000)

# cash = Cash()
# cash.pay(12000)
        
