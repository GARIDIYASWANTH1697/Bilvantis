# 1)student ={
#     "name" : "yaswanth",
#     "age"  :23,
#     "course" : "python",
#     "city"  :"hyderabad"
# }

# print(student)


# 2)student = {
#     "name": "Yaswanth",
#     "age": 23,
#     "course": "Python"
# }

# print(student["name"])
# print(student["course"])


# 3)student = {
#     "name": "Yaswanth",
#     "age": 23,
#     "course": "Python"
# }

# age = student.get("age")
# print(age)



# 4)student = {
#     "name": "Yaswanth",
#     "age": 23,
#     "course": "Python"
# }

# student.update({"Marks" : 85})
# print(student)


# 5)student = {
#     "name": "Yaswanth",
#     "age": 23,
#     "marks": 75
# }

# student.update({"marks" : 90})
# print(student)


# student = {
#     "name": "Ravi",
#     "age": 21,
#     "course": "Python",
#     "city": "Hyderabad"
# }

# 6)print(student.keys())

# 7)print(student.values())

# 8)print(student.items())

# 9)x = student.pop("age")
# print(x)



# 10)student = {
#     "name": "Ravi",
#     "age": 21
# }

# student.update({"course" : "python", "city" : "hyderabad"})
# print(student)



# 11)student = {
#     "name": "Ravi",
#     "age": 21,
#     "course": "Python"
# }

# print("email" in student)


# 12)employee = {
#     "name": "Rahul",
#     "age": 25,
#     "salary": 30000,
#     "city": "Hyderabad"
# }

# del employee[salary]
# print(employee)



# 13)product = {
#     "name": "Laptop",
#     "brand": "Dell",
#     "price": 55000,
#     "ram": "8GB"
# }

# print(len(product))



# 14)student = {
#     "name": "Ravi",
#     "age": 21
# }

# x = student.setdefault("course" ,"python")
# print(x)

# y = student.setdefault("name" , "kiran")
# print(y)




# 15)keys = ["name", "age", "course", "city"]

# student = dict.fromkeys(keys, "Not Provided")

# print(student)



# student = {
#     "name": "Yaswanth",
#     "Python": 85,
#     "SQL": 78,
#     "HTML": 90
# }

# print(student["name"])
# print(student["Python"])
# print(student['SQL'])
# print(student["HTML"])
# print(student((["Python","SQL","HTML"])))


# cart = {
#     "Laptop": 50000,
#     "Mouse": 500,
#     "Keyboard": 1000
# }

# totalprice = cart["Laptop"] + cart["Keyboard"] + cart["Mouse"]
# print("total price", totalprice)


# student = {
#     "name": "Ravi",
#     "age": 21,
#     "course": "Python",
#     "city": "Hyderabad"
# }

# student.update({"age" : 22,"course" : "python full stack","city" : "Banglore"})
# print(student)

