# • Employee Payroll System
# Create a base class Employee with attributes name and base_salary. Create two subclasses:
# 	• Manager: Receives a fixed bonus added to their base salary.
# 	• Developer: Receives an hourly bonus added to their base salary.
# Implement a calculate_payout() method in each class to demonstrate polymorphism.


class Employee():
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
        

class Manager(Employee):
    def calculate_payout(self,fixed_bonus):
        self.fixed_bonus = fixed_bonus
        return self.base_salary + fixed_bonus


class Developer(Employee):
    def calculate_payout(self,hourly_bonus,hours):
        self.hourly_bonus = hourly_bonus
        self.hours = hours
        return self.base_salary + (hourly_bonus * hours)    


obj = Manager("yaswanth",23000)
print(obj.calculate_payout(2000))

obj1 = Developer("kiran",31000)
print(obj1.calculate_payout(250,79))



# • Vehicle Fleet
# Build a base class Vehicle with a method fuel_type(). 
# Create child classes ElectricCar, DieselTruck, and HybridSuv 
# that override the fuel_type() method to return their respective fuel sources.

class Vehicle():
    def fuel_type(self):
        pass  

class ElectricCar(Vehicle):
    def fuel_type(self):
        # print("this is Electrivehicle")
        return "Electric"

class DieselTruck(Vehicle):
    def fuel_type(self):
        # print("this is Dieselvehicle ")
        return "Diesel"

class HybridSuv(Vehicle):
    def fuel_type(self):
        # print("this is Hybird")
        return "Hybrid"


s = ElectricCar()
t = DieselTruck()
u = HybridSuv()

print(s.fuel_type())
print(t.fuel_type())
print(u.fuel_type())


# E-Commerce Shopping Cart
# Create an Item class (name, price) and a ShoppingCart class. 
# The shopping cart should hold a list of items and 
# feature methods to add_item(), remove_item(), and calculate_total().

class Item():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.items = []
        

class ShoppingCart():
    def add_item(self):
        self.items.append({
            "name" : self.name,
            "price" : self.price
        })

    def remove_item(self,name):    
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)

        
    def calculate_total(self,price):
        total = 0 

        for item in self.items:
            total = total + price
            return total

obj = Item("laptop",75000)

obj.add_item()
print(obj.add_item)

obj.remove_item()
print(obj.remove_item)

obj.calculate_total()
print(obj.calculate_total)

