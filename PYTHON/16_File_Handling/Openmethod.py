# # Read a File

# # file = open("Simple.txt", "r")

# # data = file.read()

# # print(data)

# # file.close()


# # f = open("Simple","r")

# # f = open("demofile.txt")
# # print(f.readline())
# # f.close()


# file = open("Simple.txt","w")

# l = file.write("hello world this is Yash,I am learning Python")

# print(l.read())

# file.close()


# file = open("data.txt", "r")

# print(file.read())

# file.close()


# file = open('data.txt','r')

# print(file.read())

# file.close()


# file = open("data.txt", "r")

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()


file = open("data.txt", "r")

data = file.readlines()

print(data)

file.close()

file = open("data.txt", "r")

print(file.read())
print(file.read())

file.close()