# 1.Student Marks

# Accept marks for 5 subjects.
# Validate each mark between 0 and 100.
# Calculate total and average.
# If average ≥ 60 print "Good" else "Needs Improvement".


marks = []

for i in range(5):

    mark = int(input(f"Enter a marks of subject {i+1}:"))

while True:
    if mark >= 0 and mark <= 100:
        print("valid")
    else:
        print("Invalid")

total = sum(marks) 

average = total/5

if average >= 60:
    print("Good")
else:
    print("Needs improvement")    



