# 1. 🏦 Bank Account

# Create an Account class with account_holder and balance, and a Bank class.

# Methods:

# deposit(account, amount)
# withdraw(account, amount)
# check_balance(account)

# Condition: Balance kanna ekkuva withdraw cheyyakudadhu.


# class Account():
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance

# class Bank():        
#     def deposit(self,account,amount):
#         self.account = account
#         self.amount = amount
#         self.balance += self.deposit

#     def withdraw(self,account,amount):
#         self.account = account
#         self.amount = amount
#         self.balance += self.withdraw

#     def check_balance(self,account):
#         self.account = account
#         print("balance",self.balance)    

# obj = Bank("ravi",34000)

# obj = Account("ravi",2400)
# obj.withdraw()
# obj.check_balance()

class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


class Bank:
    def deposit(self, account, amount):
        account.balance += amount

    def withdraw(self, account, amount):
        if amount <= account.balance:
            account.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self, account):
        print("Balance:", account.balance)


account = Account("Ravi", 2400)

bank = Bank()

bank.deposit(account, 1000)
bank.withdraw(account, 500)
bank.check_balance(account)


# 2. Library Management

# Create a Book class with title and price, and a Library class.

# Methods:

# add_book(book)
# remove_book(title)
# calculate_total_price()

# Example:

# Book("Python", 500)
# Book("SQL", 400)
# Book("Django", 600)

# Total:

# 1500


# class Book():
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price

# class Library():
#     def add_book(self,book):
#         self.Book += book

#     def remove_book(self,title):
#         self.book -= title

#     def calculate_total_price(self):

#         return self.price    

# book = Book("python",200),
# book = Book("sql",300)
# book =Book("sprak",450)

# L = Library()
# L.add_book("Django")

# L.remove_book("sql")

# L.calculate_total_price()

    

class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0

        for item in self.items:
            total = total + item.price

        return total


item1 = Item("Laptop", 75000)
item2 = Item("Mouse", 1000)
item3 = Item("Keyboard", 2000)

cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

print("Total:", cart.calculate_total())

cart.remove_item("Mouse")

print("After removing Mouse:")
print("Total:", cart.calculate_total())

    