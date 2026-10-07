# 3.  Car Rental

# Create a Car class with model and rent_per_day, and a Rental class.

# Methods:

# add_car(car)
# remove_car(model)
# calculate_rent(days)

# Example:

# BMW → ₹3000/day
# Toyota → ₹2000/day


# class Car():
#     def __init__(self,model,rent_per_day):
#         self.model = model
#         self.rent_per_day = rent_per_day

# class Rental():
#     def __init__(self):
#         self.car =[]

#     def add_car(self,car):
#         self.car.append(car)  

#     def remove_car(self,model):
#         for car in self.car:
#             if car.model == model:
#                 self.car.remove(car)
#                 break

    
#         def calculate_rent(self, days):
#             total = 0

#             for car in self.car:
#                 total = total + car.rent_per_day * days

#             return total

# obj1 = Car("BMW",2000)
# obj2 = Car("TOYOTA",1500)

# rental = Rental()

# rental.add_car(obj1)
# rental.add_car(obj2)

# rental.remove_car("LAMBORGUNE")

# print(rental.calculate_rent(8))
        


# 4.  Student Management

# Create a Student class with name and marks, and a StudentManager class.

# Methods:

# add_student(student)
# remove_student(name)
# calculate_average()

# Example:

# Yaswanth → 80
# Ravi → 90
# Kiran → 70

# Average = 80



class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

class StudentManager():
    def __init__(self):
        self.Student = []

    def add_student(self,Student):
        self.Student.append(Student)    

    def remove_Student(self,name):
        for student in self.Student:
            if student.name == name:
                self.Student.remove(student)    

    def calculate_average(self):
        total = 0

        for student in self.Student:
            total = total+ student.marks

        return total/len(self.Student)    

stu1 = Student("kiran",85)  
stu2 = Student("prasad",87)
stu3 = Student("pinky",75)

sm = StudentManager()

sm.add_student(stu1)
sm.add_student(stu2)
sm.add_student(stu3)


sm.remove_Student("prasad")

print(sm.calculate_average())
    




# 5. Hotel Booking

# Create a Room class with room_number and price_per_day, and a Hotel class.

# Methods:

# add_room(room)
# book_room(room_number)
# calculate_bill(days)


class Room():
    def __init__(self,room_number,price_per_day):
        self.room_number = room_number
        self.price_per_day = price_per_day

class Hotel():
    def __init__(self):
        self.room = []

    def add_room(self,room):
        self.room.append(room)    

    def book_room(self,room_number):
        for room in self.room:
            if room.room_number == room_number:
                self.booked_room = room
                print("booked the room")
    
    def calculate_bill(self,days):
        total = days * self.booked_room.price_per_day
        return total

room1 = Room(101,450)
room2 = Room(102,458) 
room3 = Room(106,500)

hotel = Hotel()

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

hotel.book_room(102)

print(hotel.calculate_bill(8))



        
        




        



