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


# try:
#     a = 10
#     b = 2
#     result = a / b

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)
#     print("No exception occurred")    



try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Number cannot be zero")

else:
    print("Result:", result)

finally:
    print("Program completed")    


#1)ZERO DIVISION ERROR
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# 2) VALUE ERROR
try:
    num = int("hello")
    print(num)

except ValueError:
    print("Please enter a valid number")


# 3)TypeError — Incorrect data types    
try:
    result = 10 + "20"
    print(result)

except TypeError:
    print("Cannot add an integer and a string")



# 4. IndexError — Invalid list index
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("List index does not exist")  


# 5)KEY ERROR   
try:
    student = {"name": "Ravi", "age": 21}
    print(student["salary"])

except KeyError:
    print("Key not found in dictionary")



# 6)NameError — Undefined variable
# try:
    # print(total)

# except NameError:
    # print("Variable is not defined")


# 7)FILE NOT FOUND ERROR
try:
    file = open("abc.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File does not exist")    

 
    




