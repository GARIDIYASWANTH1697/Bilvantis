# Keys Methods
# Definition: Returns a view containing all the keys in the dictionary.


# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }

#  print(student.keys())
# s = student.keys()
# print(s)

# Values
# Definition: Returns a view containing all the values in the dictionary.

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }

# print(student.values())
# print(student.20())

# Items()
# Definition: Returns a view containing all key-value pairs as tuples.

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }

# print(student.items())

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()

# car["year"] = 2018
# car["year"] = 2020
# car["brand"] = "TATA"

# print(x)

# Get()
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.get("model")
# # y = car.get(1964)
# print(car.get("company"))


# print(x)


# UPDATE()

# student = {
#     "name" : "yaswanth",
#     "age"  : 24

# }

# # print(student.items())

# student.update({"course" : "python","age" : 25,"city" : "hyderabd"})

# print(student)

# print(student.items())

# POP()

# student = {
    # "name": "Rahul",
    # "age": 20,
    # "course": "Python"
# }

# removed = student.pop("age")

# print("Removed value:", removed)
# print(student)


# POPITEM()
# ---> It removes the last key value pair item

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }

# student.update({"age" : 30,"city" : "Mumbai"})

# removed = student.popitem()

# print("Removed:", removed)
# print(student)


# Clear()
# Definition: Removes all key-value pairs from the dictionary.

# student = {
#     "name": "Rahul",
#     "age": 20
# }

# student.clear()
# print(student)
# student.update({"name":"yaswanth","age" : 25,"course" : "python", "city" : "hyderabad"})
# print(student)



# student.items()

# print(student)

# Setdefault()

# student = {
#     "name": "Rahul",
#     "age": 20
# }

# result = student.setdefault("city", "Hyderabad")

# print(result)
# student.update({"city" : "Goa"})
# print(student)


# car = {
#   "brand": "Ford",
  
#   "year": 1964
# }

# x = car.setdefault("model", "Bronco")

# print(x)


# Fromkeys()

# keys = ["name", "age", "city"]

# student = dict.fromkeys(keys, "Not Provided")

# print(student)

# student = dict.fromkeys(keys, "now setdefault")
# print(student)
