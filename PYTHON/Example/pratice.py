x = 10        # int
pi = 3.14     # float
name = "Yaswanth"  # string
is_active = True   # boolean


for i in range(3):
    print(i)   # prints 0,1,2

if x > 5:
    print("Greater than 5")


def greet(name):
    return f"Hello, {name}!"

print(greet("Yaswanth"))


class Animal:
    def speak(self):
        print("This is an animal")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()   # Woof!




import math
print(math.sqrt(16))  # 4.0


with open("data.txt", "w") as f:
    f.write("Hello, file!")

with open("data.txt", "r") as f:
    print(f.read())



try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


x = "25"
y = int(x) + 5
print(y)


class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")


def add(a, b):
    return a + b

print(add(3, 5))   # 8

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())          # Hello, Guest!
print(greet("Yaswanth")) # Hello, Yaswanth!


def power(base, exponent):
    return base ** exponent

print(power(exponent=3, base=2))  # 8


def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))  # 10


def info(**kwargs):
    return kwargs

print(info(name="Yaswanth", age=22))
# {'name': 'Yaswanth', 'age': 22}


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120


def apply(func, value):
    return func(value)

print(apply(lambda x: x+10, 5))  # 15

