# import pandas as pd

# # Create a DataFrame from a dictionary
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "City": ["Hyderabad", "Delhi", "Mumbai"]
# }

# df = pd.DataFrame(data)

# print(df)


# import pandas as pd

# data = {
#     "score" : [20,30,40],
#     "goals" : [2,4,6]
# }

# df = pd.DataFrame(data)

# print(df)



# 2 From List of Dictionaries

import pandas as pd

data = [
    {"name":"kavya","score":87},
    {"name":"shiva","score":48}

]

df = pd.DataFrame(data)

print(df)


import pandas as pd

data = [
    {"name":"kartik","goals":3},
    {"name":"prasad","goals":5},
    {"name":"praveen","points":43}
]

df = pd.DataFrame(data)

print(df)


import pandas as pd

s1 = pd.Series([10, 20, 30], name="Math")
s2 = pd.Series([40, 50, 60], name="Science")

df = pd.DataFrame({"Math": s1, "Science": s2})
print(df)



import pandas as pd

data = {
    "students":["math","science","english"],
    "Marks":[90,85,99]
}

df = pd.DataFrame(data)

print(df)
print(df.columns)
print(df.shape)


