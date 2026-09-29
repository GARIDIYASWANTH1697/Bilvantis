# 1). Write a program that accepts a number from the user and checks whether the number is:
# * Positive
# * Negative
# * Zero

# number = int(input("enter a number"))

# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negitive")
# else:
#     print("zero")    



# 2. Accept three numbers from the user and find the largest number using conditional statements.

# num1 = int(input("enter a number"))
# num2 = int(input("enter a number"))
# num3 = int(input("enter a number"))

# if num1 > num2 and num1 > num3:
#     print("num1 is largest")
# elif num2 > num1 and num2 > num3:
#     print("num2 is largest") 
# else:
#     print("num3 is largest")       




# 3. Accept marks for a student and display the grade according to the following:

# | Marks    | Grade |
# | -- | -- |
# | 90–100   | A     |
# | 80–89    | B     |
# | 70–79    | C     |
# | 60–69    | D     |
# | Below 60 | F     |

# Also check whether the entered marks are valid. 
# For example, marks below `0` or above `100` should be treated as invalid.


# marks = int(input("enter a number"))

# if marks < 0 or marks > 100:
#     print("invaild")
# elif marks >= 90:
#     print("Grade A")    
# elif marks >= 80 :
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else :
#     print("Grade F")    
    


# 4. Write a program to determine whether a given year is a leap year.
# Hint: A leap year has a special relationship with divisibility by `4`, `100`, and `400`.

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# else:
#     print("Not a leap year")




# 5). Accept the number of electricity units consumed and calculate the bill using these rates:

# | Units           | Rate        |
# |  | -- |
# | First 100 units | ₹2 per unit |
# | Next 100 units  | ₹3 per unit |
# | Above 200 units | ₹5 per unit |

# Write a program using conditional statements to calculate the total bill.

# Example:
# Units consumed: 250
# Bill: ₹900


# units = int(input("enter a number"))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + ((units - 100) * 3)        
# else: 
#     bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

# print("total bill",bill)    






# 6. Accept three sides of a triangle. First check whether the three sides can form a valid triangle. If valid, determine whether it is:

# * Equilateral
# * Isosceles
# * Scalene

# Hint: A triangle is valid only when the sum of any two sides is greater than the third side.

# A = int(input("enter a number"))
# B = int(input("enter a number"))
# C = int(input("enter a number"))

# if A+B > C and B+C > A and C+A > B:
#     print("Valid")

#     if A==B==C:
#        print("Equilateral")
#     elif A==B or B==C or C==A:
#        print("scalane")
#     else:
#        print("Isoscaeles")

# else:
#    print("Invalid")
     




# 7. Write a program that calculates a movie ticket price based on age and show timing.

# Rules:

# | Condition       | Ticket Price |
# |  | --: |
# | Age below 5     |         Free |
# | Age 5–12        |         ₹100 |
# | Age 13–59       |         ₹200 |
# | Age 60 or above |         ₹120 |

# Additionally:

# * If the show is before 5 PM, give a ₹30 discount.
# * If the person is below 5 years, the ticket remains free.
# * Display the final ticket price.

# Example:
# Enter age: 25
# Enter show time: 3
# Final ticket price: ₹170


# age = int(input("Enter age: "))
# show_time = int(input("Enter show time: "))

# if age < 5:
#     price = 0

# elif age <= 12:
#     price = 100

# elif age <= 59:
#     price = 200

# else:
#     price = 120


# if age >= 5 and show_time < 5:
#     price = price - 30


# print("Final ticket price:", price)    