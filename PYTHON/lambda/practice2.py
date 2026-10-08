#FILTER + LAMBDA

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)



numbers = [5, 12, 8, 20, 3, 15]

result = list(filter(lambda x: x > 10, numbers))

print(result)


# Filter names starting with "A"
names = ["Anil", "Rahul", "Arjun", "Sneha", "Akhil"]

result = list(filter(lambda name: name.startswith("A"), names))

print(result)

