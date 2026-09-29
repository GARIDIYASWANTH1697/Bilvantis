# class Person:

#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello", self.name)


# class Student(Person):
#     pass

# s1 = Student("Yaswanth")
# s1.greet()


# Level 1 — Basic

# 1. Create a parent class Animal with a method eat() that prints "Animal is eating".
# Create a child class Dog that inherits from Animal. Create a Dog object and call eat().

# class Animal():

#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     pass

# d1 = Dog()
# d1.eat()


# 2. Create a parent class Person with an attribute name.
# Create a child class Student that inherits from Person. 
# Create a student object with the name "Yaswanth" and print the name.

# class Person():

#     def __init__(self,name):
#         self.name = name

# class student(Person):
#     pass

# d1 = student("Yaswanth")
# print(d1.name)



# Level 2 — Add child functionality

# 4. Create a parent class Person with a method:
# introduce()
# It should print "I am a person".
# Create a child class Student with its own method:
# study()
# It should print "I am studying".
# Using a Student object, call both methods.


# class Person():
#     def __init__(self):
#         pass

#     def introduce(self):
#         print("I am a person")

# class Student(Person):
#     def study(self):
#         print("I am studying")

# d1 = Student()
# d1.introduce()
# d1.study()


# 3. Create a parent class Vehicle with a method start() that prints "Vehicle started".
# Create a child class Car. Use the Car object to call start().

# class Vehicle():
#     def start(self):
#         print("vehicle started")

# class Car(Vehicle):
#     pass

# c = Car()

# c.start()


# 1)SINGLE INHERITANCE

# class Animal:
#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Barking")


# d = Dog()

# d.eat()
# d.bark()


# 2)MULTIPLE INHERITANCE

# class Father:
#     def skills1(self):
#         print("Driving")


# class Mother:
#     def skills2(self):
#         print("Cooking")


# class Son(Father, Mother):
#     pass


# s = Son()

# s.skills1()
# s.skills2()


# 3)MULTILEVEL INHERITANCE

# class Grandfather:
#     def property(self):
#         print("Property")


# class Father(Grandfather):
#     def car(self):
#         print("Car")


# class Son(Father):
#     def bike(self):
#         print("Bike")


# s = Son()

# s.property()
# s.car()
# s.bike()



# 4. Hierarchical Inheritance

# class Animal:
#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Barking")


# class Cat(Animal):
#     def meow(self):
#         print("Meowing")


# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()




# 5) HYBIRD HIERARCHICAL

# class Animal:
#     def eat(self):
#         print("Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Barking")


# class Cat(Animal):
#     def meow(self):
#         print("Meowing")


# class Puppy(Dog):
#     def play(self):
#         print("Playing")