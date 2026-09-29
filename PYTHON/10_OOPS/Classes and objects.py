# class Student:
#     pass

# student1 = Student()
# student2 = Student()
# student3 = Student()


# class Student:

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

# student1 = Student("Yaswanth", 23, "Python")

# print(student1.name)
# print(student1.age)
# print(student1.course)


# class Student:

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

# student1 = Student("Yaswanth", 23, "Python")
# student2 = Student("Rahul", 22, "Java")

# print(student1.name)
# print(student1.age)
# print(student1.course)

# print(student2.name)
# print(student2.age)
# print(student2.course)


# Default Value

# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age

# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)



# WITH MULTIPLE PARAMETERS

# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(self.name, "says Woof!")


# d1 = Dog("Buddy", 3)

# d1.bark()


# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(self.name, "says Woof!")

# d1 = Dog("Buddy")
# d2 = Dog("Rocky")

# d1.bark()
# d2.bark()


# class Person: 
#     def __init__(self, name): 
#         self.name = name 
 
#     def greet(self): 
#         return "Hello, " + self.name 
 
#     def welcome(self): 
#         message = self.greet() 
#         print(message + "! Welcome to our website.") 
 
# p1 = Person("Tobias") 
# p1.welcome()