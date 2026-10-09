# Print all even numbers from 1 to n using a loop.

# n = 10
# for i in range(1,n+1):
#     if i%2 == 0:
#         print(i,end=" ")

# Count the vowels in a given string.


str = "programming"
vowels = "aeiouAEIOU"
count = 0

for i in str:
    if i in vowels:
        count += 1

print(count)        
