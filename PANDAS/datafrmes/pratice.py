# 1.Create & Inspect
# Make a DataFrame with columns:

# "Student" → ["A", "B", "C"]

# "Math" → [90, 80, 70]

# "Science" → [85, 75, 65]

# Print the DataFrame.

# Print df.columns, df.index, and df.shape.


# import pandas as pd

# data = {
#     "student":["A","B","C"],
#     "Math":[90,80,70],
#     "Science":[85,75,65],
#     "English":[66,71,82]
# }

# s = pd.DataFrame(data)

# print(s)
# print(s.columns)
# print(s.index)
# print(s.shape)


# print(s["Math"])

# print(s[["Math","Science"]])

# print(s.describe())

# s["History"] = [60,73,81]

# print(s)

# print("average Math salary:",s["Math"].mean())

# print(s[s["Science"] > 80])

# 7. Mixed Data
# Create a DataFrame with columns:

# "Item" → ["Pen", "Book", "Laptop"]

# "Price" → [10, 200, 50000]

# Print df.dtypes.

# Explain why "Item" is object and "Price" is int64.


# import pandas as pd

# data = {
#     "Item" :["pen","book","laptop"],
#     "price":[10,200,50000]
# }

# df = pd.DataFrame(data)

# print(df.dtypes)

#Item is stores the onjects in string format and price store the integers