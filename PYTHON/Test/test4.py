class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        # your code
        self.items.append({
            "name" : name,
            "price" :price,
            "quantity":quantity
        })
        pass

    def display_items(self):
        # your code
        for item in self.items:
            print(item["name"],item["price"],item["quantity"])
        pass

    def calculate_total(self):
        # your code
        total = 0
        for item in self.items:
            total = total + item["price"]*item["quantity"]

        return total   
        pass

    def remove_item(self, name):
        # your code
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                break
        pass


cart = ShoppingCart()

cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 1000, 2)
cart.add_item("Keyboard", 2000, 1)

cart.display_items()

print("Total:", cart.calculate_total())

cart.remove_item("Mouse")

print("After removing Mouse:")
cart.display_items()

print("Total:", cart.calculate_total())




# Book Repository
# Create a Book class with attributes like title, author, and price. 
# Include a method named display_details() 
# that prints out a well-formatted summary of the book.


class Book():
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("book details")  
        print("TITLE",self.title)
        print("AUTHOR",self.author)
        print("PRICE",self.price)

obj = Book("pyhton","John gresham",550)
obj.display_details()          


# Circle Geometry
# Design a Circle class that takes a radius during initialization. 
# Add two methods: calculate_area() and calculate_circumference(). 
# Use Python's math module for π.    
import math

class Circle():
    def __init__(self,radius):
        self.radius = radius
        pass

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        print("Area of circle",area)
        pass

    def calculate_circumference(self):
        C = 2 * math.pi * self.radius
        print("Circumference", C)
        pass

obj = Circle(5)    
obj.calculate_area()
obj.calculate_circumference()


# • Smartphone Upgrade
# Create a Smartphone class with attributes brand, model, and storage. 
# Add a method upgrade_storage(amount) that increases the storage capacity by the given amount.

class Smartphone():
    def __init__(self,brand,model,storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def upgrade_storage(self,amount):
        self.storage += amount

obj = Smartphone("oppo","s12",120)
obj.upgrade_storage(2000)        
print(obj.storage)

    