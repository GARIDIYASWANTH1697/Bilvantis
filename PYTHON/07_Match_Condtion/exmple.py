#Simple rule: match-case is especially useful when you have one value and many possible cases.

# Syntex

# match value:
#     case pattern1:
#         # code
#     case pattern2:
#         # code
#     case _:
#         # default code



# day = 2

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid day")



# day = 2

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Invalid")



# day = 2

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid")