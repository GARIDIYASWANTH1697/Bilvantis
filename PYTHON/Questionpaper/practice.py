# 11. Write a Python program to check whether a given string is a palindrome (ignore upper/lower case). 

# Input: Madam 

# Output: True

# str = "MadaM"

# if str == str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")    


#SECOND LARGEST

# numbers = [10, 25, 8, 40, 30]

# largest = second_largest = float('-inf')

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num!= largest:
#         second_largest = num

# print("Second largest number:", second_largest)

# largest = second_largest = float('-inf')

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("second_largest:", second_largest)      



# numbers = [10, 25, 8, 40, 30]

# largest = max(numbers)

# numbers.remove(largest)

# second_largest = max(numbers)

# print(second_largest)


#  Write a Python program using lambda with filter() and map() to get all words longer than 4 characters
# from a list and convert them to upper case. 

# Original list: ['sun', 'python', 'code', 'java', 'program'] 

# Output: ['PYTHON', 'PROGRAM'] 

# words = ['sun', 'python', 'code', 'java', 'program'] 

# result = list(map(lambda x : x.upper(),filter(lambda x : len(x)>4,words)))

# print(result)




# 14. Write a Python program to create a Student class with attributes name and marks (a list). 
# Implement a method average() that returns the average marks and a method grade() that returns: 

# A if average >= 90, B if average >= 75, C if average >= 50, otherwise F. 

# Input: Student("Ravi", [85, 78, 92]) 

# Output: Ravi 85.0 B
 
class student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avarage(self):
        return  sum(self.marks)/len(self.marks)

    def grade(self):
        if self.avarage() >= 90:
            return "Grade A"
        elif self.avarage() >= 75:
            return "Grade B"
        elif self.avarage() >= 50:
            return "Grade C"
        else:
            print("FAIL")



obj = student("Ravi",[85,79,92])

print(obj.name, obj.avarage(), obj.grade())



# 15. Write a generator function fibonacci(n) that yields the first n Fibonacci numbers. 
# Print them using a for loop. 

# Input: n = 7 

# Output: 0 1 1 2 3 5 8



def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num, end=" ")     





