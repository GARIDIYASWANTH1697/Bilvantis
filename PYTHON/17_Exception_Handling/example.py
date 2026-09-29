# a = 10
# b = 0

# print(a / b)
# print("Program completed")


# try:
#     a = 10
#     b = 0
#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# print("Program completed")


# Value Eerror Handling

# try:
#     age = int("hello")
#     print(age)

# except ValueError:
#     print("Please enter a valid number")


# numbers = [10, 20, 30]

# try:
#     print(numbers[6])

# except IndexError:
#     print("Index does not exist")


try:
    a = 10
    b = 2
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
    print("No exception occurred")    