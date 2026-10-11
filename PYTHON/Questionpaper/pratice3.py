# Write a Python program to find how many times each character appears in the
# stringbelow using loops. Also print the characters that occur more than once.
# text = 'programming'

text = "programming"

count = {}

for i in text:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1    
    
print(count)


# Write a Python program to calculate electricity bills.
# Requirements:
# Accept the number of customers, then use a loop to accept the units consumed byeach customer.
# Validate the units. If units are less than 0, display 'Invalid units' and ask again.
# Energy charge: first 100 units at ₹5 per unit, next 100 units (101–200) at ₹7 per unit,above 200 units at ₹10 per unit.
# Add a fixed charge of ₹50.
# If the energy charge is more than ₹1000, add a 5% surcharge on the energy charge.
# Display units, energy charge, surcharge and total bill for each customer. At the end,display the customer with the highest bill.

customers = int(input("Enter number of customers: "))

highest_bill = -1
highest_customer = 0

for i in range(1, customers + 1):

    # Validate units
    units = int(input(f"Enter units for customer {i}: "))

    while units < 0:
        print("Invalid units")
        units = int(input(f"Enter units again for customer {i}: "))

    # Calculate energy charge
    if units <= 100:
        energy = units * 5

    elif units <= 200:
        energy = 100 * 5 + (units - 100) * 7

    else:
        energy = 100 * 5 + 100 * 7 + (units - 200) * 10

    # Calculate surcharge
    if energy > 1000:
        surcharge = energy * 0.05
    else:
        surcharge = 0

    # Calculate total bill
    total = energy + surcharge + 50

    # Display bill
    print("\nCustomer:", i)
    print("Units:", units)
    print("Energy charge: ₹", energy)
    print("Surcharge: ₹", surcharge)
    print("Total bill: ₹", total)

    # Find highest bill
    if total > highest_bill:
        highest_bill = total
        highest_customer = i

print("\nCustomer with highest bill:", highest_customer)
print("Highest bill amount: ₹", highest_bill)



# Write a Python program that accepts the bill amounts for 4 different months from a user and calculates the total
# expenditure, average monthly bill, and usage category.
# Requirements:
# - Use a loop to accept amounts for 4 months.
# - Validate each input: If less than 0, display 'Invalid amount' and ask again.
# - Calculate: Total amount and Average amount.
# - Determine category using if-elif-else:
# Average >= 5000 -> 'High User'
# Average >= 3000 -> 'Medium User'
# Below 3000 -> 'Low User'
# - The user gets a 'Cashback Eligible' status only if all months have bills >= 1000. If even on
# e month is below 1000, display 'NOT ELIGIBLE FOR CASHBACK' regardless of average.

bills = []

for i in range(1, 5):
    amount = float(input(f"Enter bill for month {i}: "))

    while amount < 0:
        print("Invalid amount")
        amount = float(input(f"Enter bill for month {i} again: "))

    bills.append(amount)

total = sum(bills)
average = total / 4

print("Total expenditure:", total)
print("Average monthly bill:", average)

if average >= 5000:
    print("High User")
elif average >= 3000:
    print("Medium User")
else:
    print("Low User")

if all(amount >= 1000 for amount in bills):
    print("Cashback Eligible")
else:
    print("NOT ELIGIBLE FOR CASHBACK")



# Write a Python program that accepts product scores (out of 100) given by 5 different
# reviewers for a product and
# calculates statistics.
# Requirements:
# - Use a loop to accept 5 scores.
# - Validate: if score < 0 or > 100, display 'Invalid score' and re-ask.
# - Calculate: Total and Average rating.
# - Tag using if-elif-else: >=85 'Excellent', >=70 'Good', >=50 'Average', Below 50 'Poor'.
# - Certified Safe badge only if all individual reviews are >= 50. Otherwise, 'REJECT CERTIFICAT
# ION' regardless of average.

total = 0

for i in range(1,6):

    score = int(input(f"enter the product score {i}:"))

    while score < 0:
        print("invalid score")
        score = int(input(f"enter the score {i}:"))

total += score

average = total/5

print("Total score", total)
print("Average",average)

if score >= 85:
    print("Good")
elif score >= 50:
    print("Avaerge")
else: 
    print("poor")    



if score >= 50:
    print("Certified safe")
else:
    print("REJECT CERTIFICATION")    






