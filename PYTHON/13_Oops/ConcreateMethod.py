# from abc import ABC, abstractmethod

# class Animal(ABC):
#     # Abstract method (no body)
#     @abstractmethod
#     def make_sound(self):
#         pass

#     # Concrete method (has body)
#     def sleep(self):
#         print("Sleeping...")

# class Dog(Animal):
#     # Must implement abstract method
#     def make_sound(self):
#         print("Woof!")

# # Using the class
# d = Dog()
# d.make_sound()  # Woof!
# d.sleep()       # Sleeping...


# Concrete Method with simple Example

# class Calculator:
#     def add(self, a, b):   # Concrete method
#         return a + b

# calc = Calculator()
# print(calc.add(5, 3))  # Output: 8






# concrete method with abstract method class

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     def fuel_type(self):   # Concrete method
#         print("Uses petrol or diesel")

# class Car(Vehicle):
#     def start(self):
#         print("Car started")

# c = Car()
# c.start()       # Car started
# c.fuel_type()   # Uses petrol or diesel





# Concrete method with logic

# class Student:
#     def grade(self, marks):   # Concrete method
#         if marks >= 50:
#             return "Pass"
#         else:
#             return "Fail"

# s = Student()
# print(s.grade(75))  # Output: Pass



# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass

#     def receipt(self):
#         print("Receipt generated")


# class UPI(Payment):

#     def pay(self, amount):
#         print("Paid using UPI:", amount)


# u = UPI()

# u.pay(500)
# u.receipt()


