
# age = int(input("Enter age: "))
# time = int(input("Enter show time (24-hour format): "))

# if age < 0 or time < 0 or time > 23:
#     print("Invalid input")
# elif age < 5:
#     price = 0
# elif age <= 12:
#     price = 100
# elif age <= 59:
#     price = 200
# else:
#     price = 120

#     # Apply discount after selecting the age-based price
# if age >= 5 and time < 17 and age >= 0 and time <= 23:
#     price = price - 30
#     print("Final ticket price: ₹", price)
# elif age >= 0 and time >= 0 and time <= 23:
#     print("Final ticket price: ₹", price)





# def check_password(password):
#     if len(password) < 6:
#         strength = "Weak"
#     elif len(password) <= 9:
#         strength = "Medium"
#     else:
#         strength = "Strong"

#     has_digit = any(ch.isdigit() for ch in password)

#     if not has_digit:
#         return strength + " - Must contain a digit"

#     return strength

# print(check_password("abc"))
# print(check_password("python7"))
# print(check_password("python12345"))


# square = map(lambda x: x * x)
# print(square(6))


# orders = [
#     {'order_id': 1, 'customer': 'Ravi', 'amount': 2500},
#     {'order_id': 2, 'customer': 'Anu', 'amount': 800},
#     {'order_id': 3, 'customer': 'John', 'amount': 4500},
#     {'order_id': 4, 'customer': 'Priya', 'amount': 1200},
#     {'order_id': 5, 'customer': 'Kiran', 'amount': 3500}
# ]

# result = list(filter(lambda amount: amount>1000, orders))
# print(result)

# orders = filter(sort())

