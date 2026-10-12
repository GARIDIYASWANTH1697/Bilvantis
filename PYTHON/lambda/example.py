employees = [
    {'id': 102, 'name': 'Alice', 'salary': 70000},
    {'id': 103, 'name': 'Bob', 'salary': 60000},
    {'id': 101, 'name': 'John', 'salary': 50000}
]

highest = max(employees, key=lambda emp: emp['salary'])

print(highest)

print("Name:", highest['name'])
print("Salary:", highest['salary'])

employees.sort(key=lambda x: x["salary"], reverse=True)
print(employees)
print(employees[0])
# print(employees["name"])
names = list(map(lambda x: x["name"], employees))
print(names)