#LIST COMPREHENSION

numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]

print(squares)


#LIST COMPREHENSION WITH if
numbers = [1,2,3,4,5,6]

even = [n for n in numbers if n % 2 == 0]

print(even)



#WITH STRINGS
names = ["john", "alice", "bob"]

upper_names = [name.upper() for name in names]

print(upper_names)



# WITH DICTIONARY
employees = [
    {"id": 101, "name": "John", "salary": 50000},
    {"id": 102, "name": "Alice", "salary": 70000},
    {"id": 103, "name": "Bob", "salary": 60000}
]

names = [emp["name"] for emp in employees]

print(names)


#WITH SQUARE
numbers = [1, 2, 3, 4, 5]

result = [x ** 2 for x in numbers]

print(result)


#WITH CUBE
numbers = [1, 2, 3, 4, 5]

cubes = [x ** 3 for x in numbers]

print(cubes)


#GET ONLY EVEN NUMBERS
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = [x for x in numbers if x % 2 == 0]

print(even)


#GET ONLY ODD NUMBERS
numbers = [1, 2, 3, 4, 5, 6, 7]

odd = [x for x in numbers if x % 2 != 0]

print(odd)