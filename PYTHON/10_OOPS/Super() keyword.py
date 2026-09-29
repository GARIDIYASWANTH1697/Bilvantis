
# With keyword

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("Person constructor")


# class Student(Person):
#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course


# s1 = Student("Yaswanth", "Python")

# print(s1.name)
# print(s1.course)





# Without Keyword

# class Person:
#     def __init__(self, name):
#         self.name = name


# class Student(Person):
#     def __init__(self, name, course):
#         self.course = course


# s1 = Student("Yaswanth", "Python")

# print(s1.name)

# it gives the error


# Level 1 — Basic



# 1. Person → Student

# Create a parent class Person with:

# name
# age

# Create a child class Student with:
# course
# Requirements:
# Use __init__() in both classes.
# Use super() in the Student class.
# Create a Student object.
# Print name, age, and course.

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age,course):
#         super().__init__(name, age)   
#         self.course = course

# obj = Student("Ravi",32,"python")

# print(obj.name)
# print(obj.age)
# print(obj.course)



# 2)class Animal():
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def eat(self):
#         super().eat()
#         print("Dog is eating")

# obj = Dog()
# obj.eat()




# class Employee():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         pass


# class Developer(Employee):
#     def __init__(self, name, age,programming_language):
#         super().__init__(name, age)
#         self.programming_language = programming_language

# obj = Developer("Aravind",35,"java")
# print(obj.name)
# print(obj.age)
# print(obj.programming_language)        
