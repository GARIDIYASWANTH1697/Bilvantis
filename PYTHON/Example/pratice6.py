class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


b = B()
b.show()



class Employee:
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class TeamLead(Manager, Developer):
    pass


t = TeamLead()

t.work()


class student():
    def study(self):
        print("He is studying")

class stu1(student):
    def study(self):
        print("He is writing")

class stu2(student):
    def study(self):
        print("He is reading")

class allof(stu1,stu2):
    pass

s = allof()
s.study()



                        