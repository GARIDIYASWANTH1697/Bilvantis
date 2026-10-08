# 1.Student Marks

# Accept marks for 5 subjects.
# Validate each mark between 0 and 100.
# Calculate total and average.
# If average ≥ 60 print "Good" else "Needs Improvement".

# marks = []

# for i in range(5):

#     while True:    
#         mark = int(input(f"Enter a marks of subject {i+1}:"))


#         if mark >= 0 and mark <= 100:
#             print("valid")
#         else:
#             print("Invalid")

# total = sum(marks) 
# average = total/5

# print("Total",total)
# print("Average",average)

# if average >= 60:
#     print("Good")
# else:
#     print("Needs improvement")    


# Positive / Negative

# Accept 5 numbers.
# Count how many are positive, negative, and zero.

# P = 0
# N = 0
# Z = 0

# for i in range(5):

#     # while True:
#         numbers = int(input(f"enter the subject marks{i + 1}:"))

#         if numbers > 0:
#             print("positive")
#             P += 1
        
#         elif numbers < 0:
#             print("negitive")
#             N += 1
        
#         else:
#             print("zero")       
#             Z += 1

# print("Positive number",P)
# print("Negitive number",N)
# print("zeros",Z)


# 3. Sum and Average

# Accept marks of 5 subjects.
# Calculate total and average.

# mark = []

# for i in range(5):

#     marks =int(input(f"enter the subject marks{i + 1}:"))
#     mark.append(marks)

# total = sum(mark)
    
# average = total/len(mark)

# print(total)
# print(average)



# Multiplication Table

# Accept a number from the user.
# Print its multiplication table from 1 to 10.

# num = []

# for i in range(10):
#     number = int(input(f"enter the numbers{i + 1}:"))
#     num .append(number)

# for i in num:
#     print("2 *", i, "=", num*i)


# 5. Student Grade
# Accept marks of 5 subjects.

# Calculate:

# Total
# Average
# Grade

# Grade:

# 90+  → A
# 75+  → B
# 60+  → C
# 50+  → D
# Below 50 → F

# Also, if any subject < 40, print FAIL.

marks = []

for i in range(5):

    while True:
        mark = int(input(f"enter the subject marks{i+1}:"))

        if mark < 0 and marks > 100:
            print("Invalid")
        else:
            marks.append(mark)  
            break  

total = sum(marks)
average = total/len(marks)

print("Total marks",total)
print("Average marks", average)


if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 60:
    print("Grade C")
elif average >= 50:
    print("Grade D")
else:
    print("FAIL")        
 

if all (mark >= 40 for mark in marks):
    print("PASSED")
else:
    print("FAILED")    
