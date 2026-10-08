# map(lambda x: x * 2, [1, 2, 3])
# print(map)  

# numbers = [1, 2, 3, 4, 5]

# result = map(lambda x: x * 2, numbers)

# print(list(result))



# numbers = [1, 2, 3, 4, 5, 6]

# result = filter(lambda x: x % 2 == 0, numbers)

# print(list(result))


# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# result = reduce(lambda a, b: a + b, numbers)

# print(result)



# Question 1: The String Reverser
# Write a lambda function that takes a single string as an 
# argument and returns it reversed. Assign it to a variable named 
# reverse_str and test it with "python".
# # • Expected Output: "nohtyp"

# str = "python"

# reverse_str =lambda str:str[::-1]
# print(reverse_str("python"))


# Question 2: Conditional Maximum
# Write a lambda function that takes two numeric arguments and returns 
# the larger of the two. Do not use the built-in max() function; 
# use an if-else ternary expression instead.
# • Expected Input: max_val(12, 45)
# • Expected Output: 45

# max_val = lambda a,b : a if a > b else b
# print(max_val(12,45))



# • Problem: Write a lambda function that takes two numbers, x and y, 
# and returns their product. Assign it to a variable named multiply and call it.
# • Expected Output: multiply(5, 6) should return 30.

multiply = lambda a,b: a * b
print(multiply(5,6))


#  Check Even or Odd
# • Problem: Write a lambda function that returns True if a given number is even, and False if it is odd.
# • Expected Output: Passing 7 should return False; passing 10 should return True.

value = lambda a:"Even" if a%2 == 0 else "odd"
print(value(7))
print(value(10))

# String Manipulation
# • Problem: Create a lambda function that takes a string and returns it in all uppercase letters.
# • Expected Output: Passing "hello" should return "HELLO".

str = lambda s: s.upper()
print(str("hello"))

# Filtering Even Numbers
# • Problem: Given the list numbers = [1, 5, 4, 6, 8, 11, 3, 12], 
# use the built-in filter() function along with a lambda expression to extract only the even numbers. 
# Convert the result back to a list.
# • Expected Output: [4, 6, 8, 12]

numbers = [1, 5, 4, 6, 8, 11, 3, 12]

result = filter(lambda x:x%2 == 0,numbers)

print(list(result))


# Mapping Cubes
# • Problem: Given the list nums = [1, 2, 3, 4, 5],
# use map() and a lambda function to compute the cube (x³) of every number in the list.
# • Expected Output: [1, 8, 27, 64, 125]

nums = [1,2,3,4,5]

result = map(lambda x:x**3,nums)

print(list(result))


# Lambda with Ternary Operators
# • Problem: Write a single lambda function that takes two numbers and returns
# the larger number. Hint: Use Python's inline if-else syntax (a if condition else b).
# • Expected Output: Passing 15 and 42 should return 42

result = lambda x,y:x if x > y else y
print(result(15,42))