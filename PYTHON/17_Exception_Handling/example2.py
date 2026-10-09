
# try:
#     num = int(input("enter the number"))
#     print("interger",num)
    
# except ValueError:
#     print("That was not a valid integer. Please enter a number.")

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("cannot divisible by zero")
        return None
print(safe_divide(10,0))       
print(safe_divide(10,2)) 



filename = "missing_file.txt"

try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("file not found ,try again in another path")   


items = ["apple", "banana", "cherry"]

try:
    print(items[5])
except IndexError:
    print("index is not found")    







    
