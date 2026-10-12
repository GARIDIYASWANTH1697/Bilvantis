# 1. Student Marks and Grade
# Easy

# A program accepts marks for 6 subjects.
# Requirements:
# - Use a loop to accept marks for all 6 subjects.
# - If marks are below 0 or above 100, print "Invalid marks" and ask again.
# - Calculate total and average.
# - Grade: average ≥ 85 → A, ≥ 70 → B, ≥ 50 → C, otherwise F.
# - The student passes only if every subject has marks ≥ 35.
# Sample: Marks = 90, 80, 70, 60, 50, 40
# Expected: Total = 390, Average = 65.0, Grade = C, Result = PASS

# marks = [90,80,70,60,50,40]
# total = 0
# passed = True

# for i in range(1,7):
#     while True:
#         marks = int(input(f"enter the marks{i}:"))

#     if marks < 0 or marks > 100:
#         print("Invalid marks")
#     else:
#         print("valid")
        

# total = sum(marks)

# average = total/len(marks) 

# print("Total marks",total)
# print("average marks",average)

# if average >= 85:
#     grade = "A"
# elif average >= 75:
#     grade = "B"
# elif average >= 50:
#     grade = "C"
# else:
#      grade = "F"           

# if passed:
#     print("PASS")
# else:
#     print("FAIL")


# Ask how many customers there are.
# For each customer, input electricity units consumed.
# If units are negative, print "Invalid units" and ask again.

# Calculate the energy charge:
# - First 100 units: ₹5 per unit
# - Next 100 units: ₹7 per unit
# - Above 200 units: ₹10 per unit

# Add a fixed charge of ₹50.
# If the energy charge is greater than ₹1,000, add a 5% surcharge on the energy charge.
# Display each customer's units, energy charge, surcharge, and total bill.
# At the end, display the customer with the highest bill.


# n = int(input(f"enter number of custmers:"))

# highest_bil = 0
# highest_customer = 0

# for i in range(1,n+1):
#     units = int(input(f"enter the units{i}:"))

#     if units < 0:
#         print("Invalid units")
#     else:
#         break

# # calculate energy charge
# if units <= 100:
#     energy_charge = units*5
# elif units >= 100:
#     energy_charge = (100*5)+(units-100)*7
# else             


# numbers = [10, 20, 30, 40]

# it = iter(numbers)

# print(next(it))
# print(next(it)+next(it))
# print(next(it))
# print(next(it))


def numbers():
    yield 1
    yield 2
    yield 3

result = numbers()
print(result)    


def numbers():
    yield 1
    yield 2
    yield 3

result = numbers()

print(next(result))
print(next(result))
print(next(result))



