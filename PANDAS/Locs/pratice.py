# import pandas as pd

# data = {
#     "Name": ["A", "B", "C"],
#     "Age": [25, 30, 35]
# }
# df = pd.DataFrame(data, index=["x", "y", "z"])

# print(df)


# print(df.loc["y", "Age"])   # → 30
# print(df.loc[:, "Name"])    # → All names (A, B, C)



# print(df.iloc[1, 1])        # → 30 (row 1, column 1)
# print(df.iloc[:, 0])        # → All names (A, B, C)



# import pandas as pd

# data = {
#     "Names" : ["kiran","prashanth","swamy","venu","sushanth"],
#     "age"   : [23,24,23,27,21],
#     "course": ["python","sql","java","databricks","javascript"],
#     "Marks" : [68,87,59,80,91]
# }

# df = pd.DataFrame(data, index = ["A","B","C","D","E"])

# print(df)

# print(df.loc["A","course"])

# print(df.loc["D","Marks"])

# print(df.iloc[2,3])


# 1.1. Display the complete row for index 'b'.
# print(df.loc["B"])

# 1.2. Display the first row using its position.
# print(df.iloc[0])

# 1.3. Display only the Name column using loc.
# print(df.loc["A","Names"])


# 1.4. Display only the Marks column using iloc.
# print(df.iloc[:,3])

# 2.4. Display Name and Course for indexes 'a', 'd', and 'e'.

# print(df.loc[["A","D","E"],["Names","course"]])



#2.1. Display the Name and Marks of index 'c'.

# print(df.loc["C"],["Names","Marks"])


# 2.2. Display the first three rows.

# print(df.iloc[:3])

# 2.3. Display rows at positions 1 and 3.








