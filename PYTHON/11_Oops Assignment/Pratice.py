# class BankAccount():
#     def __init__(self,account_number,holder_name,balance):
#         self.account_number
#         self.holder_name
#         self.balance

#     def deposit(self,amount):
#         balance = balance + amount    
#         self.balance = self.balance + 



# 2.Create an Employee Payroll System using multilevel inheritance:

# Person
#    ↓
# Employee
#    ↓
# Manager

# Requirements:
# Person → name, age
# Employee → employee ID, basic salary
# Manager → bonus, team size
# Calculate the final salary.
# Override a method such as calculate_salary() in Manager.
# Create objects for both employees and managers.

# class person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Employee(person):
#     def __init__(self, name, age,employee_id,basic_salary):
#         super().__init__(name, age)
#         self.employee_id = employee_id
#         self.basic_salary = basic_salary

#     def Calculate_salary(self):
#         return self.basic_salary

# class Manager(Employee):
#     def __init__(self, name, age, employee_id, basic_salary,bonus,team_size):
#         super().__init__(name, age, employee_id, basic_salary)  
#         self.bonus = bonus
#         self.team_size = team_size 

#     def Calculate_salary(self):
#             return self.basic_salary + self.bonus


# d1 = Employee("Yaswanth",24,"BITNI006",30000)
# c1 = Manager("Yaswanth",24,"BITNI006",30000,20000,8)             
        
# print(d1.Calculate_salary())
# print(c1.Calculate_salary())




