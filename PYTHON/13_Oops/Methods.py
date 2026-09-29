# 1)Instance Method 

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def student(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
        
            


# s1 = Student("Yaswanth", 23)
# s2 = Student("srikar",25)

# s1.display()
# s2.diaplay()


# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Yaswanth", 23)

# s1.display()



# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):   #Instance Method
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Yaswanth", 23)

# s1.display()


# Instance Method with multiple Methods

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_name(self):       # Instance method
#         print(self.name)

#     def display_age(self):        # Instance method
#         print(self.age)

#     def introduce(self):          # Instance method
#         print("My name is", self.name)

# s1 = Student("Yaswanth", 23)

# s1.display_name()
# s1.display_age()
# s1.introduce()    



# Class Methods

# class Student:

#     college = "ABC College"
#     course = "Python"
#     students_count = 100

#     @classmethod
#     def display_college(cls):
#         print("College:", cls.college)

#     @classmethod
#     def display_course(cls):
#         print("Course:", cls.course)

#     @classmethod
#     def display_count(cls):
#         print("Students:", cls.students_count)


# Student.display_college()
# Student.display_course()
# Student.display_count()


# now compare with Instance variable

# class Student:

#     college = "ABC College"

#     def __init__(self, name):
#         self.name = name

#     def display_name(self):       # Instance method
#         print(self.name)

#     @classmethod
#     def display_college(cls):     # Class method
#         print(cls.college)

# s1 = Student("Yaswanth")

# s1.display_name()        

# print(s1.college)

# cls is not compulsory as a name, but the first parameter is required for a class method.

# @classmethod
# def display_college(x):
#     print(x.college)