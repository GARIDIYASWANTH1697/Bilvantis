class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


obj = Dog()
obj.sound()




class Vehicle():
    def starts(self):
        print("Vehicle starts")

class Car(Vehicle):
    def starts(self):
        print("Car starts")        

obj = Car()
obj.starts()



# Question 2 — Different Child Classes

# Create a parent class Employee with:

# work()

# Print:

# Employee is working

# Create two child classes:

# Developer
# Manager

# Both should override work().

# Developer should print:

# Developer writes code

# Manager should print:

# Manager manages the team

# Create objects of both classes and call work().

# Expected output:

# Developer writes code
# Manager manages the team

class Employee():
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Manager(Employee):
    def work(self):
        print("manager manages the team")                

s1 = Developer()
s1.work()

s2 = Manager()
s2.work()




# Question 3 — Overriding + super()

# Create a parent class Person with a method:

# display()

# Print:

# This is a person

# Create a child class Student that overrides display().

# Inside the child's display():

# Call the parent's display() using super().
# Then print:
# This is a student

# Expected output:

# This is a person
# This is a student

# 💡 Hint for Q3:

# super().display()

# Try all 3 and send me your code. I'll check each one.


class Person():
    def display(self):
        print("this is a person")

class Student(Person):
    def display(self):
        super().display()
        print("this is a student")

s4 = Student()
s4.display()