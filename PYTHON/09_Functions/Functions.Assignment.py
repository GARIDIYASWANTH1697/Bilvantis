# 1. Create a function: check_number(num)
# The function should return:
# * `"Even"` if the number is even.
# * `"Odd"` if the number is odd.
# * `"Zero"` if the number is zero.
# Example:
# check_number(25)
# Output: Odd


# def check_number(num):

#     if num == 0:
#         return "Zero"

#     elif num % 2 == 0:
#         return "Even"

#     else:
#         return "Odd"

# print(check_number(25))



# 2. Create a function: find_largest(a, b, c)
# The function should return the largest of the three numbers.
# **Restriction:** Do not use `max()`.
# Example:
# find_largest(25, 10, 18)
# Output: 25


# def find_largest(a, b, c):

#     if a >= b and a >= c:
#         return a

#     elif b >= a and b >= c:
#         return b

#     else:
#         return c

# print(find_largest(25, 10, 18))


# 3. Create a function: calculate_grade(marks)
# Rules:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# Below 60 → F
# If the marks are less than `0` or greater than `100`, return:
# Invalid Marks


# def calculate_grade(marks):

#     if marks < 0 or marks > 100:
#         return "Invalid Marks"

#     elif marks >= 90:
#         return "A"

#     elif marks >= 80:
#         return "B"

#     elif marks >= 70:
#         return "C"

#     elif marks >= 60:
#         return "D"

#     else:
#         return "F"

# print(calculate_grade(85))


# 4. Create a function: login(username, password)
# The function should check whether:
# Username = "admin"
# Password = "python123"
# If both are correct, return:
# Login Successful
# If the username is incorrect, return:
# Invalid Username
# If the username is correct but the password is incorrect, return:
# Invalid Password


# def login(username, password):

#     if username != "admin":
#         return "Invalid Username"

#     elif password != "python123":
#         return "Invalid Password"

#     else:
#         return "Login Successful"


# print(login("admin", "python123"))



# 5. Create:calculate_bill(units)
# Calculate the electricity bill using:
# First 100 units  → ₹2/unit
# 101–200          → ₹3/unit
# Above 200        → ₹5/unit
# The function should return the final bill.
# **Important:** Calculate the bill progressively.
# For example, for `250` units:
# First 100  → 100 × 2
# Next 100   → 100 × 3
# Remaining  → 50 × 5

# def calculate_bill(units):

#     if units <= 100:
#         return units * 2

#     elif units <= 200:
#         return (100 * 2) + ((units - 100) * 3)

#     else:
#         return (100 * 2) + (100 * 3) + ((units - 200) * 5)

# print(calculate_bill(250))


# 6. Create:calculator(a, b, operator)
# Support:
# +
# -
# *
# /
# %
# **
# Example:
# calculator(10, 3, "%")
# Output:
# 1
# Handle division by zero appropriately.


# def calculator(a, b, operator):

#     if operator == "+":
#         return a + b

#     elif operator == "-":
#         return a - b

#     elif operator == "*":
#         return a * b

#     elif operator == "/":
#         if b == 0:
#             return "Cannot divide by zero"
#         return a / b

#     elif operator == "%":
#         if b == 0:
#             return "Cannot divide by zero"
#         return a % b

#     elif operator == "**":
#         return a ** b

    # else:
        # return "Invalid Operator"

# print(calculator(10, 3, "%"))


# 7. Create: check_password(password)
# The function should check the password length and return:
# "Strong"
# "Medium"
# "Weak"
# Rules:
# * Length less than 6 → Weak
# * Length 6–9 → Medium
# * Length 10 or more → Strong
# **Bonus:** Also check whether the password contains at least one digit.


# def check_password(password):

#     if len(password) < 6:
#         return "Weak"

#     elif len(password) <= 9:
#         return "Medium"

#     else:
#         return "Strong"

# print(check_password("hello123"))



# 8. Create: generate_username(first_name, last_name)
# The function should:
# 1. Remove unnecessary spaces.
# 2. Convert the names to lowercase.
# 3. Take the first three characters of the first name.
# 4. Take the first three characters of the last name.
# 5. Join them to create a username.
# Example:
# First name: Rahul
# Last name: Sharma
# Output:
# rahsha
# Use string methods and slicing.


# def generate_username(first_name, last_name):

#     first_name = first_name.strip().lower()
#     last_name = last_name.strip().lower()

#     username = first_name[:3] + last_name[:3]

#     return username

# print(generate_username("Rahul", "Sharma"))



# 9. Create: ticket_price(age, show_time)
# Rules:
# Age below 5       → Free
# Age 5–12          → ₹100
# Age 13–59         → ₹200
# Age 60 or above   → ₹120
# Additional rule:
# If the show is before `5 PM`, give a ₹30 discount.
# The discount should **not** be applied to free tickets.
# Example:
# ticket_price(25, 3)
# Output:
# 170

# def ticket_price(age, show_time):

#     if age < 5:
#         return "Free"

#     elif age <= 12:
#         price = 100

#     elif age <= 59:
#         price = 200

#     else:
#         price = 120

#     if show_time < 5:
#         price = price - 30

#     return price

# print(ticket_price(25, 3))


# 10. Create: triangle_type(a, b, c)
# First determine whether the three sides form a valid triangle.
# If valid, return:
# Equilateral
# Isosceles
# Scalene
# If invalid, return:
# Invalid Triangle
# Example:
# triangle_type(10, 10, 10)
# Output:
# Equilateral


# def triangle_type(a, b, c):

#     if a + b <= c or a + c <= b or b + c <= a:
#         return "Invalid Triangle"

#     elif a == b and b == c:
#         return "Equilateral"

#     elif a == b or b == c or a == c:
#         return "Isosceles"

#     else:
#         return "Scalene"

# print(triangle_type(10, 10, 10))



# 11. Create: calculate_discount(amount, membership)
# Discount rules:
# Amount >= 10000 → 20%
# Amount >= 5000  → 10%
# Amount >= 2000  → 5%
# Below 2000      → No discount
# If the customer is a member, provide an **additional 5% discount**.
# Return the final amount after applying the discount.
# Example:
# calculate_discount(6000, True)

# def calculate_discount(amount, membership):

#     if amount >= 10000:
#         discount = 20

#     elif amount >= 5000:
#         discount = 10

#     elif amount >= 2000:
#         discount = 5

#     else:
#         discount = 0

#     if membership:
#         discount = discount + 5

#     discount_amount = amount * discount / 100

#     final_amount = amount - discount_amount

#     return final_amount

# print(calculate_discount(6000, True))



# 12. Create: is_valid_date(day, month, year)
# Check whether the given date is valid.
# Consider:
# * Months with 30 days
# * Months with 31 days
# * February
# * Leap years
# Examples:
# 29/02/2024 → Valid
# 29/02/2023 → Invalid
# 31/04/2025 → Invalid
# 31/12/2025 → Valid
# **Challenge:** Do not use any date/time library.

# def is_valid_date(day, month, year):

#     if month < 1 or month > 12:
#         return "Invalid"

#     if day < 1:
#         return "Invalid"

#     # February
#     if month == 2:

#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             max_days = 29
#         else:
#             max_days = 28

#     # 30-day months
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         max_days = 30

#     # 31-day months
#     else:
#         max_days = 31

#     if day <= max_days:
#         return "Valid"
#     else:
#         return "Invalid"


# print(is_valid_date(29, 2, 2024))
# print(is_valid_date(29, 2, 2023))
# print(is_valid_date(31, 4, 2025))
# print(is_valid_date(31, 12, 2025))



# 13. Create: withdraw(balance, amount)
# Rules:
# * Amount must be greater than `0`.
# * Amount must be a multiple of `100`.
# * Minimum balance after withdrawal must be ₹500.
# * Withdrawal cannot exceed the available balance.
# Return an appropriate message for each situation.
# Example:
# Balance: ₹5000
# Withdrawal: ₹2000
# Output:
# Withdrawal successful
# Remaining balance: ₹3000

# def withdraw(balance, amount):

#     if amount <= 0:
#         return "Amount must be greater than 0"

#     elif amount % 100 != 0:
#         return "Amount must be a multiple of 100"

#     elif amount > balance:
#         return "Insufficient balance"

#     elif balance - amount < 500:
#         return "Minimum balance of ₹500 must be maintained"

#     else:
#         remaining_balance = balance - amount

#         return "Withdrawal successful\nRemaining balance: ₹" + str(remaining_balance)

# print(withdraw(5000, 2000))




# 14. Create: analyze_number(num)
# The function should determine:
# * Whether the number is positive, negative, or zero.
# * Whether it is even or odd.
# * Whether it is divisible by both 3 and 5.
# Return/display all the results.
# Example:
# Number: 30
# Positive
# Even
# Divisible by both 3 and 5

# def analyze_number(num):

#     if num > 0:
#         print("Positive")

#     elif num < 0:
#         print("Negative")

#     else:
#         print("Zero")


#     if num % 2 == 0:
#         print("Even")

#     else:
#         print("Odd")


#     if num % 3 == 0 and num % 5 == 0:
#         print("Divisible by both 3 and 5")

#     else:
#         print("Not divisible by both 3 and 5")

# analyze_number(30)



# 15. Create the following functions:
# calculate_total(m1, m2, m3)
# calculate_average(total)
# calculate_grade(average)
# check_result(m1, m2, m3)
# display_result(name, m1, m2, m3)
# Rules:
# A student passes only if:
# * Each subject mark is at least `35`.
# * Overall average is at least `40`.
# Grade:
# 90+     → A
# 80–89   → B
# 70–79   → C
# 60–69   → D
# 40–59   → E
# Below 40 → F
# `display_result()` should call the other functions and produce:
# Student Name: Rahul
# Total: 255
# Average: 85
# Result: PASS
# Grade: B

# def calculate_total(m1, m2, m3):

#     return m1 + m2 + m3


# def calculate_average(total):

#     return total / 3


# def calculate_grade(average):

#     if average >= 90:
#         return "A"

#     elif average >= 80:
#         return "B"

#     elif average >= 70:
#         return "C"

#     elif average >= 60:
#         return "D"

#     elif average >= 40:
#         return "E"

#     else:
#         return "F"


# def check_result(m1, m2, m3):

#     total = calculate_total(m1, m2, m3)
#     average = calculate_average(total)

#     if m1 >= 35 and m2 >= 35 and m3 >= 35 and average >= 40:
#         return "PASS"

#     else:
#         return "FAIL"


# def display_result(name, m1, m2, m3):

#     total = calculate_total(m1, m2, m3)
#     average = calculate_average(total)
#     result = check_result(m1, m2, m3)
#     grade = calculate_grade(average)

#     print("Student Name:", name)
#     print("Total:", total)
#     print("Average:", average)
#     print("Result:", result)
#     print("Grade:", grade)


# display_result("Rahul", 85, 85, 85)