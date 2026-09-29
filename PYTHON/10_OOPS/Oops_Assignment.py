
# 1)Simple Class with an Attribute

# class Student:
#     pass


# # Creating an object
# s1 = Student()

# # Adding an attribute to the object
# s1.name = "Yaswanth"
# s1.course = "Python"

# # Accessing attributes
# print(s1.name)
# print(s1.course)



# 2)class with __init__ constructor

# class Person:

#     def __init__(self, name, age):
#         # Store values inside the current object
#         self.name = name
#         self.age = age


# # Creating an object and passing values
# p1 = Person("Tobias", 25)

# # Accessing object attributes
# print(p1.name)
# print(p1.age)


# 3)class with multiple Objects

# class Car:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color


# # Creating two different objects
# car1 = Car("Toyota", "White")
# car2 = Car("BMW", "Black")

# # Accessing attributes of each object
# print(car1.brand, car1.color)
# print(car2.brand, car2.color)


# 4)class with attribute and methods

# class Dog:

#     def __init__(self, name):
#         self.name = name

#     # Method
#     def bark(self):
#         print(self.name, "says Woof!")


# # Creating an object
# d1 = Dog("Buddy")

# # Calling the object's method
# d1.bark()


# 5)class with multiple methods each calling each method

# class Person:

#     def __init__(self, name):
#         self.name = name

#     # First method
#     def greet(self):
#         return "Hello, " + self.name

#     # Second method calls the first method
#     def welcome(self):
#         message = self.greet()
#         print(message + "! Welcome to our website.")


# # Creating an object
# p1 = Person("Tobias")

# # Calling the welcome method
# p1.welcome()