# names = ["Ravi", "Anil", "Kiran", "Bhanu", "Zoya"]

# names.sort()

# print(names)




# students = [
#     ("Rahul", 85),
#     ("Priya", 92),
#     ("Arjun", 78),
#     ("Sneha", 88)
# ]

# students.sort(key=lambda x: x[1])

# print(students)

# students.sort(key=lambda x:x[1], reverse = True)

# print(students)


# students = [
#     {"name": "Rahul", "marks": 85},
#     {"name": "Priya", "marks": 92},
#     {"name": "Arjun", "marks": 78}
# ]

# students.sort(key=lambda x: x["marks"],reverse=True)

# print(students)



# # 1. Given the following list: 

employees = [ 

     {"id": 101, "name": "John", "salary": 50000}, 

     {"id": 102, "name": "Alice", "salary": 70000}, 

     {"id": 103, "name": "Bob", "salary": 60000} 

] 

# Perform the following operations: 

# Find the employee with the highest salary. 

# Sort employees by salary in descending order. 

# Create a new list containing only employee names. 

# employees.sort(key=lambda x: x["salary"], reverse=True)
# print(employees[0])

# employees.sort(key=lambda x: x["salary"], reverse=True)
# print(employees)

# names = [x["name"] for x in employees]
# print(names)




products = [ {'code': 'P101', 'name': 'Pen', 'price': 10, 'stock': 120}, 
            {'code': 'P102', 'name': 'Notebook', 'price': 45, 'stock': 30}, 
            {'code': 'P103', 'name': 'Bag', 'price': 850, 'stock': 15},
              {'code': 'P104', 'name': 'Marker', 'price': 25, 'stock': 40}]
# Perform the following operations:
# Find the most expensive product.
# Sort the products by stock in ascending order.
# Create a new list containing the names of products whose stock is less than 50.

# products.sort(key=lambda x: x["price"], reverse=True)
# print(products)
# print(products[0])

# products.sort(key=lambda x: x["price"])
# print(products)

# products.sort(key=lambda x: x["name"])
# print(products)



# Given the following list of transactions:
transactions = [ ('T1', 'Credit', 5000),
                 ('T2', 'Debit', 2000), 
                 ('T3', 'Credit', 3000), 
                 ('T4', 'Debit', 1500)]
# Perform the following operations:
# Find the total credit amount and the total debit amount.
# Find the transaction with the largest amount.
# Create a new list containing only the IDs of debit transactions.
# Sort the transactions by amount in descending order.
# 2.
# Write a Python program to find the duplicate elements in a list and

# transactions.sort(key=lambda x: x[1])
# print(transactions)
# result = add([0][1])+add([2][3])
# print(result)