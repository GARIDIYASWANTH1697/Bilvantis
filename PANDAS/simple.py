# Print multiplication table for a given number
num = 5

print(f"Multiplication Table of {num}")
for i in range(1, 11):   # loop from 1 to 10
    result = num * i
    print(f"{num} x {i} = {result}")
