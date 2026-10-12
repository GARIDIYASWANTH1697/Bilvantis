# 2. Library Management
# Easy
# Create a class Library.
# Requirements:
# - add_book(book) — add a book.
# - remove_book(book) — remove a book.
# - display_books() — display available books.
# - If a book is not found, print "Book not found".

class Library:
    def __init__(self):
        self.book = []

    def add_book(self,book):
        self.book.append(book)  
        print("Book added successfully")

    def remove_book(self,book):
        if book in self.book:
            self.book.remove(book)  
            print("Book remove successfully")    

    def display_books(self):
        print("display_books",self.book)        


# if book not in self.book:
    print("Book not found")
# else:
    print("Book found")    



# Question 3: Bank Account — Easy to Medium
# BankAccount ane class create cheyyi.
# Requirements:
# - deposit(amount) — balance ki amount add cheyyali.
# - withdraw(amount) — balance nunchi amount subtract cheyyali.
# - Balance kanna ekkuva amount withdraw chesthe "Insufficient balance" ani print cheyyali.
# - display_balance() — current balance display cheyyali.
# - Starting balance ₹1000 undali.
# Hint: __init__() lo self.balance = 1000 use cheyyi.

class Bankaccount():
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("amount added succussfully")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")      

    def display_balance(self):
        print("Display_balance",self.balance)        


obj = Bankaccount(1000)
obj.deposit(500)
obj.withdraw(1000)
obj.display_balance()    

# Question 4: Product Management (OOP)
# Product ane class create cheyyi.
# - add_stock(quantity) — stock ki quantity add cheyyali.
# - remove_stock(quantity) — stock nunchi quantity subtract cheyyali.
# - Stock saripokapothe "Insufficient stock" print cheyyali.
# - display_stock() — current stock display cheyyali.
# - Starting stock 10 undali.
# Hint: Bank account lo balance use chesinattu, ikkada stock use cheyyi.

class Product():
    def __init__(self):
        self.stock = 10

    def add_stock(self,quantity):
        self.stock += quantity

    def remove_stock(self,quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Insufficent stock")

    def display_stock(self):
        print("stock",self.stock)            

obj=Product()
obj.add_stock(50)
obj.remove_stock(10)
obj.display_stock()

        
# Library class raayi:
# - add_book(book) — book add cheyyali.
# - remove_book(book) — book unte remove cheyyali, lekapothe "Book not found" print cheyyali.
# - display_books() — books display cheyyali.
# - Starting list empty ga undali.


class Library():
    def __init__(self):
        self.book = []

    def add_book(self,book):
        self.book.append(book)

    def remove_book(self,book):
        if book in self.book:
            self.book.remove(book)
            print("Book removed successfully")
        else:
            print("Book not found")

    def display_books(self):
        print("display books",self.book)

obj = Library()
obj.add_book("python")
obj.add_book("SQL")
obj.remove_book("SQL")
obj.display_books()
        