# numbers = [10, 20, 30, 40]

# print(numbers)


# numbers = [10, 20, 30, 40]

# for num in numbers:
    # print(num)



# numbers = [10, 20, 30, 40]

# my_iterator = iter(numbers)

# print(my_iterator)



# numbers = [10, 20, 30, 40]

# it = iter(numbers)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# numbers = [10, 20, 30]

# it = iter(numbers)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



# numbers = [10, 20, 30]

# for num in numbers:
#     print(num)

# it = iter(numbers)

# while True:
#     try:
#         num = next(it)
#         print(num)
#     except StopIteration:
#         break



# class Numbers:

#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.num <= 5:
#             value = self.num
#             self.num += 1
#             return value
#         else:
#             raise StopIteration


# obj = Numbers()

# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))


# numbers = [10, 20, 30, 40]

# my_iterator = iter(numbers)

# print(my_iterator)


# numbers = [10, 20, 30, 40]

# it = iter(numbers)

# print(it)


class Numbers:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


obj = Numbers()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))