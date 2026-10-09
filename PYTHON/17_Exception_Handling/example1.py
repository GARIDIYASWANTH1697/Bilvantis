# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     result = a / b
#     print("Result:", result)

# except ValueError:
#     print("Enter numbers only")

# except ZeroDivisionError:
#     print("Cannot divide by zero")



# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Number cannot be zero")

# else:
#     print("Result:", result)

# finally:
#     print("Program completed")


# USING RAISE

# try:
#     age = int(input("Enter your age: "))

#     if age < 18:
#         raise ValueError("Age must be 18 or above")

#     print("Eligible")

# except ValueError as e:
#     print("Error:", e)    



# 10)Write a program to divide 10 by 0. Handle the error and print `Cannot divide by zero`.
# try:
#     a = 10
#     b = 0
#     result = a/b

# except ZeroDivisionError:
#     print("Cannot divide by zero") 


# try:
#     age = int("age")
#     print(age)

# except ValueError:
#     print("Invalid number")    


# numbers = [10, 20, 30]
# try:
#     print(numbers[5])
# except IndexError:
#     print("Index does not exist")


# Challenge 1: Safe Division Utility
# Write a function safe_divide(a, b) that takes two arguments.
# • It should attempt to divide a by b and return the result.
# • Handle ZeroDivisionError by returning a descriptive string (e.g., "Error: Cannot divide by zero").
# • Handle TypeError if a user passes non-numeric values (like strings) and return "Error: Invalid input types".

# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except TypeError:
#         # age = int("hello")
#         print("Invalid")    

# safe_divide(10,0)
# safe_divide(100,"hello")


# Challenge 2: Robust Integer Input Loop
# Write a script that continuously prompts the user to enter a whole number using input().
# • If the user enters something that isn't a valid integer, 
# catch the ValueError and print "That's not a number! Please try again."
# • The loop should only break once a valid integer is entered. 
# Print that integer back to the user before ending.

# num = int(input("enter a number"))

# try:
#     result = num("hello")
#     print(result)
# except ValueError:
#     print("That's not a numner")
# else:
#     print("integer back to the user")    


# while True:
#     try:
#         num = int(input("enter the number"))
#         print("integer",num)
#         break

#     except ValueError:
#         print("that's not a number,try again")