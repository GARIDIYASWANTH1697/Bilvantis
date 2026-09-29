# # 1. Positive → Even or Odd

# # Write a program that:
# # Checks whether a number is positive.
# # If positive, checks whether it is even or odd.
# # If not positive, prints "Not a positive number".

# # Example: num = 8


# num = 8

# if num > 0:
#     print('positive')
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("Not a positive number")            



# 2. Age → Child or Teenager

# Write a program that:
# Checks whether age is greater than 0.
# If valid, checks:
# Age <= 12 → "Child"
# Age <= 19 → "Teenager"
# Otherwise → "Adult"
# If age is not greater than 0, print "Invalid age".
# Example: age = 15


# age = 15

# if age > 0:
#     print("valid")
#     if age <= 12:
#         print("Child")
#     elif age <= 19:
#         print("Teenager")
#     else:
#         print("Adult")
# else:
#     print("Invaild")                



#  3. Number → Positive → Greater than 100

# Write a program that:
# Checks whether a number is positive.
# If positive:
# If number is greater than 100, print "Greater than 100".
# Otherwise, print "100 or below".
# If not positive, print "Not a positive number".
# Example: num = 150

# num = 150

# if num > 0:
#     print("positive")
#     if num > 100:
#         print("Greater than 100")
#     else:
#         print("100 or below")
# else:
#     print("Not a positive number")            



# 5)username = "admin"
# password = "1234"

# if username == "admin" and password == "1234":
#     print("Login Successfully")
# elif username == "admin" and password != "1234":
#     print("Invalid username")





# 6. ATM Withdrawal
# Write a program that:
# Checks whether the PIN is correct.
# If PIN is correct, checks whether the withdrawal amount is less than or equal to the balance.
# If balance is sufficient, print "Withdrawal successful".
# Otherwise, print "Insufficient balance".
# If PIN is wrong, print "Incorrect PIN".


# pin = 1234
# balance = 5000
# amount = 2000
        


# if pin == 1234:
#     if amount <= balance:
#         print("Withdrawal successfully")
#     else:
#         print("Insufficient balance")
# else:
#     print("Incorrect pin")            