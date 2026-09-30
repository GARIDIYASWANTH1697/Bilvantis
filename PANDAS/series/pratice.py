# Create & Inspect
# Create a Series from the list [11, 12, 13, 14, 16].

# Print the Series.

# Show its index, values, dtype, and shape.


# import pandas as pd

# s = pd.Series([11,12,13,14,16])

# print(s)
# print(s.index)
# print(s.dtype)
# print(s.shape)
# print(s.at[2])


# 2.Custom Index
# Make a Series with values [100, 200, 300] and index labels ["x", "y", "z"].

# Access the value at label "y".

# Access the first element using position.


# import pandas as pd

# s = pd.Series([100,200,300], index = ("X","Y","Z"))

# print(s)
# print(s.values)
# print(s.index[0])





# 3.Dictionary to Series
# Convert the dictionary {"math": 90, "science": 85, "english": 95} into a Series.

# Print the Series.

# Show the dtype and explain why it is int64.

# import pandas as pd

# data = {"math":90,"science":85,"english":95}

# s = pd.Series(data)

# print(s)

#here int64 is 2 power 64 bits 



# 4. Mixed Data Types
# Create a Series with values ["apple", 10, 3.5].

# Print the Series.

# Check the dtype.

# Why is it object?

import pandas as pd

s = pd.Series(["apple",10,3.5])

print(s)
print(s.dtype)

