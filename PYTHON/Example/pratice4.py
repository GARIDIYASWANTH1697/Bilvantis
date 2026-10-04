# numbers = [10,20,30,40]

# x = iter(numbers)

# print(next(x))
# print(next(x))
# print(next(x))

# print(next(x))
# print(next(x))


def numbers():
    yield 10
    yield 20
    yield 30

x = numbers()

print(next(x))

print(next(x))
print(next(x))
print(next(x))


class Employee():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Bankaccount(self,salary,course):
        self.salary = salary
        self.course = course

object = Employee("yash",24)

object.Bankaccount(20000,"Python")


class student():

    college = "ABC college"        #class variable
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def employee(self):            #instance method
        pass

    @staticmethod
    def bankaccount():             #static method
        pass

    @classmethod
    def show_details(cls):               #class method
        pass    


from abc import ABC, abstractmethod

class student(ABC):

    @abstractmethod
    def student_pass(self):
        pass
        
class employee(student):
    def calculate_salary(self):
        print("salary credited")

    def salary_credit(self):
        print("salary credited")   

obj = employee()

obj.calculate_salary()
obj.salary_credit()



class student():
    def __init__(self,name):
        self.name = name
        
class employee(student):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary = salary

obj = employee("yaswanth",20000)

print(obj.name)
print(obj.salary)


class parent():
    def __init__(self,name):
        self.name =name

class student(parent):
    def __init__(self, name,age):
        super().__init__(name)        
        self.age = age

obj = student("yaswanth",23)

print(obj.name)
print(obj.age)


class Animal():
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

obj1 = Dog()
obj1.sound()


class Employee():
    def __init__(self,name,company):
        self.name = name
        self.company = company

class Developer(Employee):
    def __init__(self, name, company,salary):
        super().__init__(name, company)        
        self.salary = salary

s = Developer("aravind","accenture",20000)

print(s.name)
print(s.company)
print(s.salary)

        