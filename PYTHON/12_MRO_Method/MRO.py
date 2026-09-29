# MRO METHOD

# class Father:
#     def skills(self):
#         print("Driving")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class Child( Mother,Father):
#     pass

# c = Child()
# c.skills()


# MRO with single Inheritance
# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     pass

# d = Dog()
# d.eat()



# MRO with Overridding

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# d = Dog()
# d.sound()        

# MRO AND SUPER()

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# class D(B, C):
#     def show(self):
#         print("D")
#         super().show()

# d = D()
# d.show()        



# same method with init and parametres

# class Bank:
#     def __init__(self, bank_name):
#         self.bank_name = bank_name

#     def details(self):
#         print("Bank:", self.bank_name)


# class SavingsAccount(Bank):
#     def __init__(self, bank_name, account_number):
#         super().__init__(bank_name)
#         self.account_number = account_number

#     def details(self):
#         print("Account Number:", self.account_number)
#         super().details()


# class PremiumAccount(Bank):
#     def __init__(self, bank_name, account_number, premium):
#         super().__init__(bank_name, account_number)
#         self.premium = premium

#     def details(self):
#         print("Premium:", self.premium)
#         super().details()


# class Customer(SavingsAccount, PremiumAccount):
#     def __init__(self, name, bank_name, account_number, premium):
#         super().__init__(bank_name, account_number, premium)
#         self.name = name

#     def details(self):
#         print("Customer:", self.name)
#         super().details()


# c = Customer("Yaswanth", "ABC Bank", 12345, "Gold")
# c.details()