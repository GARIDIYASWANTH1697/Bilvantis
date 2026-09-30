# import pandas as pd

# # Create a simple Series
# numbers = pd.Series([10, 20, 30, 40, 50])

# print(numbers)


# import pandas as pd

# marks = pd.Series([85, 90, 78])

# print(marks)



# import pandas as pd

# marks = pd.Series(
#     [85, 90, 78],
#     index=["Yaswanth", "Ravi", "Kiran"]
# )

# print(marks)


# import pandas as pd

# marks = pd.Series(
#     [85, 90, 78],
#     index=["Yaswanth", "Ravi", "Kiran"]
# )

# print(marks)


# import pandas as pd

# # From a list
# s = pd.Series([10, 20, 30, 40])
# print(s)



# Custom Index

# import pandas as pd

# s = pd.Series([10,20,40]), Index = ["a","b","c"]

# print(s)


# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)



# import pandas as pd

# s = pd.Series([11,22,33,44], index = ["w","x","y","z"])
# print(s)


# import pandas as pd

# x = pd.Series([10,20,30,40], index = ["a","b","c","d"])
# print(x)


# import pandas as pd

# a = pd.Series([10,20,30,40], index = ["a","b","c"]) #Its get ValueError 

# print(a)


# From dictionary

# import pandas as pd

# keyvalues = {"apple":1,"banana":2,"cherry":3,"dragonfruit":4}

# s = pd.Series(keyvalues)

# print(s)



# import pandas as pd

# values = {1:"cricket",2:"football",3:"volleyball",4:"kabaddi"}

# c = pd.Series(values)

# print(c)


import pandas as pd

keys = {"Bilvantis":1,"TCS":2,"wipro":3,"cognizant":"a"}

s = pd.Series(keys)

print(s)