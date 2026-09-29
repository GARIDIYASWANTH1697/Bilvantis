# Polymorphism means “one name, many forms.”

# Poly → Many
# Morphism → Forms


# polymorphism with Methods

# class Dog:
#     def speak(self):
#         print("Dog says: Woof")


# class Cat:
#     def speak(self):
#         print("Cat says: Meow")


# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()



# polymorphism with Inheritance

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def speak(self):
#         print("Dog says Woof")


# class Cat(Animal):
#     def speak(self):
#         print("Cat says Meow")


# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()



# 3. Same Function, Different Data Types

# Python's built-in functions also demonstrate polymorphism.

# print(len("Yaswanth"))
# print(len([10, 20, 30]))
# print(len((10, 20, 30)))

# the same function len()






# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()




