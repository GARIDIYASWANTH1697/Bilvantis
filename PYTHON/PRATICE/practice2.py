# 6. Marks Validation

# Accept marks for 5 subjects.

# Rules:

# Marks must be between 0 and 100.
# If invalid, print "Invalid marks" and ask again.
# After valid marks are entered, calculate the total and average.

# Hint: Use while inside for.

# marks = []

# for i in range(5):

#     while True:
#         mark = int(input(f"enter the subject marks{i + 1}:"))

#         if mark < 0 or mark > 100:
#             print("Invalid marks")
#         else: 
#             marks.append(mark)
#             break

# total = sum(marks)
# average = total/len(marks)

# print("total marks",total)
# print("average marks",average)


# 7. Student Result System ⭐

# Accept marks for N students.

# For each student:

# Accept 5 subject marks
# Validate marks
# Calculate total
# Calculate average
# Determine grade
# Print PASS/FAIL

# This combines almost everything you've learned.

# students = []

# for i in range(N):

# n = int(input("Enter number of students: "))

# for student in range(n):

#     print(f"\nStudent {student + 1}")

# marks = []

# for subject in range(5):

#     mark = int(input(f"enter the subject {subject+ 1}:"))

#     if mark < 0 or mark > 100:
#             print("Invalid marks")
#     else: 
#         marks.append(mark)
#         break

# total = sum(marks)
# average = total/len(marks)

# print("total marks",total)
# print("average marks",average)


# if average >= 90:
#     print("Grade A")
# elif average >= 75:
#     print("Grade B")
# elif average >= 60:
#     print("Grade C")
# elif average >= 50:
#     print("Grade D")
# else:
#     print("FAIL")        
 

# if all (mark >= 40 for mark in marks):
#     print("PASSED")
# else:
#     print("FAILED")    



# Level 3 — Challenge

# 8. Find Highest and Lowest Marks

# Accept marks of 5 subjects and find:

# Highest mark
# Lowest mark
# Total
# Average

# Don't use max() or min().

marks =[]
Highest_marks = marks[0]
Lowest_marks = marks[0]
# marks = []

for i in range(5):

    mark = int(input(f"enter the subject marks{i + 1}:"))
    mark.append(marks)

for s in marks:
    if s < Lowest_marks:
        Lowest_marks = s
    if s > Highest_marks:
        Highest_marks = s

total = sum(marks)
average = total/len(marks)

print("Highest",Highest_marks)
print("Lowest_marks",Lowest_marks)

print("total",total)
print("average",average)
    



