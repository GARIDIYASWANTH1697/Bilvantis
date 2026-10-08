numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)


numbers = [5, 2, 8, 1, 3]

numbers.sort(reverse=True)

print(numbers)

students = [
    ("John", 25),
    ("Alice", 20),
    ("Bob", 23)
]

students.sort(key=lambda x: x[1])

print(students)


employees = [
    ("Rahul", 50000),
    ("Priya", 70000),
    ("Arjun", 45000),
    ("Sneha", 60000)
]

employees.sort(key=lambda x : x[1] )
print(employees)


#1)SORT NUMBERS
numbers = [45, 12, 78, 3, 56, 9]

numbers.sort()

print(numbers)


#2)SORT NUMBERS IN  REVERSE
numbers = [23, 87, 12, 45, 9, 67]
numbers.sort(reverse=True)
print(numbers)


#3)SORT NAME BY ALPHABETICALLY
names = ["Ravi", "Anil", "Kiran", "Bhanu", "Zoya"]

names.sort()

print(names)


#4)SORT BY LENGTH
words = ["python", "is", "very", "easy", "language"]

words.sort(key=lambda x:len(x))

print(words)


# 5)Sort by length — longest first
words = ["cat", "elephant", "dog", "tiger", "hippopotamus"]

words.sort(key=lambda x:len(x), reverse=True)

print(words)


#6)SORT BY MARKS by using TUPLE
students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Arjun", 78),
    ("Sneha", 88)
]

students.sort(key=lambda x: x[1])

print(students)



#7)SORT STUDENT MARKS FROM HIGHEST TO LOWEST
students.sort(key=lambda x: x[1], reverse=True)

print(students)



#8)SORT EMPLOYEES BY SALARY
employees = [
    ("Rahul", 50000),
    ("Priya", 70000),
    ("Arjun", 45000),
    ("Sneha", 60000)
]

employees.sort(key=lambda x: x[1], reverse=True)

print(employees)


#9)SORT DIC BY ITS VALUE
students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Arjun", "marks": 78}
]

students.sort(key=lambda x: x["marks"])

print(students)


# 1. Given the following list: 

employees = [ 

    {"id": 101, "name": "John", "salary": 50000}, 

    {"id": 102, "name": "Alice", "salary": 70000}, 

    {"id": 103, "name": "Bob", "salary": 60000} 

] 

# Perform the following operations: 
# Find the employee with the highest salary. 
# Sort employees by salary in descending order. 
# Create a new list containing only employee names.

highest_salary = max(employees, key=lambda x: x["salary"])
print(highest_salary)

employees.sort(key=lambda x: x["salary"], reverse=True)
print(employees)

names = [employee["name"] for employee in employees]
print(names)