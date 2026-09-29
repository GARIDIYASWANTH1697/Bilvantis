# 3. Inheritance

# Create two real-world examples for each type of inheritance in Python.

# For every example:

# Use the self keyword appropriately.
# Use the super() function where applicable.
# Clearly demonstrate the relationship between the parent and child classes.
# Execute the methods and display the expected output.

# Cover the following types of inheritance:

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


# Single Inheritance
# Example1

# class Father:

#     def father_info(self):
#         print("Father: Ravi")


# class Mother:

#     def mother_info(self):
#         print("Mother: Lakshmi")


# class Child(Father, Mother):

#     def child_info(self):
#         print("Child: Rahul")


# c1 = Child()

# c1.father_info()
# c1.mother_info()
# c1.child_info()



# Example 2
# class Vehicle:

#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         print(self.brand, "vehicle is starting")


# class Car(Vehicle):

#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def display(self):
#         self.start()
#         print("Model:", self.model)


# c1 = Car("Toyota", "Innova")

# c1.display()



# Multiple Inheritance
# Example 1

# class Father:

#     def father_info(self):
#         print("Father: Ravi")


# class Mother:

#     def mother_info(self):
#         print("Mother: Lakshmi")


# class Child(Father, Mother):

#     def child_info(self):
#         print("Child: Rahul")


# c1 = Child()

# c1.father_info()
# c1.mother_info()
# c1.child_info()



# Example 2
# class Camera:

#     def take_photo(self):
#         print("Taking a photo")


# class Phone:

#     def make_call(self):
#         print("Making a phone call")


# class Smartphone(Camera, Phone):

#     def use_phone(self):
#         print("Using smartphone")


# s1 = Smartphone()

# s1.take_photo()
# s1.make_call()
# s1.use_phone()


# 3 .Multilevel inheritance

# class Person:

#     def __init__(self, name):
#         self.name = name

#     def display_person(self):
#         print("Name:", self.name)


# class Employee(Person):

#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id

#     def display_employee(self):
#         self.display_person()
#         print("Employee ID:", self.employee_id)


# class Manager(Employee):

#     def __init__(self, name, employee_id, team_size):
#         super().__init__(name, employee_id)
#         self.team_size = team_size

#     def display_manager(self):
#         self.display_employee()
#         print("Team Size:", self.team_size)


# m1 = Manager("Yaswanth", "M101", 8)

# m1.display_manager()


# # 4.Hierarchial Inheritance

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name, "is eating")


# class Dog(Animal):

#     def bark(self):
#         print(self.name, "is barking")


# class Cat(Animal):

#     def meow(self):
#         print(self.name, "is meowing")


# d1 = Dog("Tommy")
# c1 = Cat("Kitty")

# d1.eat()
# d1.bark()

# c1.eat()
# c1.meow()


# # 5.Hybird inheritance

# class Person:

#     def __init__(self, name):
#         self.name = name

#     def person_info(self):
#         print("Name:", self.name)


# class Employee(Person):

#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id

#     def employee_info(self):
#         print("Employee ID:", self.employee_id)


# class Developer(Employee):

#     def coding(self):
#         print(self.name, "is coding")


# class Manager(Employee):

#     def managing(self):
#         print(self.name, "is managing")


# class TeamLead(Developer, Manager):

#     def team_lead_info(self):
#         print(self.name, "is a Team Lead")


# t1 = TeamLead("Yaswanth", "E101")

# t1.person_info()
# t1.employee_info()
# t1.coding()
# t1.managing()
# t1.team_lead_info()

