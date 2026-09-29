# import pandas as pd

# data = {
#     "Name": ["Yaswanth", "Ravi", "Kiran"],
#     "Age": [23, 24, 22],
#     "Marks": [85, 90, 78]
# }

# df = pd.DataFrame(data)

# print(df)


# csv = pd.read_csv("students.csv")
# print(csv)


import pandas as pd

# Create data
data = {
    "Name": ["Yaswanth", "Ravi", "Kiran"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Export: save DataFrame to CSV
df.to_csv("students.csv", index=False)

print("CSV file created successfully!")

# Import: read the CSV file
new_df = pd.read_csv("students.csv")

print(new_df)


df.to_excel("students.xlsx", index=False)


df2 = pd.read_excel("students.xlsx")
print(df2)