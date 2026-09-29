# 4. Car Management System

# Design a Car parent class with appropriate variables and methods representing real-world car functionality.

# Requirements:

# Define suitable instance variables using self.
# Create multiple methods inside the Car class.
# Create appropriate child classes that inherit from the Car class.
# Use super() wherever required.
# Override methods in the child classes where appropriate.
# Create objects for the child classes.
# Execute all relevant parent and child methods.
# Display the output for each method execution.
# Clearly demonstrate how inheritance and method overriding work in your implementation.



# ```python
# class Car:

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print(self.brand, self.model, "is starting")

#     def stop(self):
#         print(self.brand, self.model, "is stopped")

#     def accelerate(self):
#         print(self.brand, self.model, "is accelerating")

#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)


# class ElectricCar(Car):

#     def __init__(self, brand, model, year, battery):
#         super().__init__(brand, model, year)
#         self.battery = battery

#     # Method Overriding
#     def start(self):
#         print(self.brand, self.model, "starts silently using electric power")

#     def charge(self):
#         print(self.brand, self.model, "is charging")

#     def display_battery(self):
#         print("Battery:", self.battery, "kWh")


# class SportsCar(Car):

#     def __init__(self, brand, model, year, top_speed):
#         super().__init__(brand, model, year)
#         self.top_speed = top_speed

#     # Method Overriding
#     def start(self):
#         print(self.brand, self.model, "starts with a powerful engine sound")

#     def turbo(self):
#         print(self.brand, self.model, "turbo mode activated")

#     def display_speed(self):
#         print("Top Speed:", self.top_speed, "km/h")


# # Creating objects

# electric_car = ElectricCar("Tesla", "Model 3", 2025, 75)

# sports_car = SportsCar("BMW", "M4", 2025, 290)


# # Electric Car methods

# print("----- Electric Car -----")

# electric_car.display_info()
# electric_car.start()
# electric_car.accelerate()
# electric_car.charge()
# electric_car.display_battery()
# electric_car.stop()


# print()

# # Sports Car methods

# print("----- Sports Car -----")

# sports_car.display_info()
# sports_car.start()
# sports_car.accelerate()
# sports_car.turbo()
# sports_car.display_speed()
# sports_car.stop()
# ```

# ### Expected Output

# ```text
# ----- Electric Car -----

# Brand: Tesla
# Model: Model 3
# Year: 2025
# Tesla Model 3 starts silently using electric power
# Tesla Model 3 is accelerating
# Tesla Model 3 is charging
# Battery: 75 kWh
# Tesla Model 3 is stopped


# ----- Sports Car -----

# Brand: BMW
# Model: M4
# Year: 2025
# BMW M4 starts with a powerful engine sound
# BMW M4 is accelerating
# BMW M4 turbo mode activated
# Top Speed: 290 km/h
# BMW M4 is stopped
# ```

# ### Where is `self`?

# We use `self` to store and access **object-specific data**.

# ```python
# self.brand
# self.model
# self.year
# ```

# For example:

# ```python
# electric_car.brand
# ```

# contains:

# ```text
# Tesla
# ```

# while:

# ```python
# sports_car.brand
# ```

# contains:

# ```text
# BMW
# ```

# So each object has its own values.

# ### Where is `super()`?

# In `ElectricCar`:

# ```python
# super().__init__(brand, model, year)
# ```

# This calls the `Car` constructor.

# The same happens in `SportsCar`:

# ```python
# super().__init__(brand, model, year)
# ```

# So we don't have to rewrite:

# ```python
# self.brand = brand
# self.model = model
# self.year = year
# ```

# inside every child class.

# ### Where is inheritance?

# ```python
# class ElectricCar(Car):
# ```

# and

# ```python
# class SportsCar(Car):
# ```

# Both inherit from `Car`.

# Therefore, the children can directly use:

# ```python
# display_info()
# accelerate()
# stop()
# ```

# without defining them again.

# ### Where is method overriding? ⭐

# Parent:

# ```python
# class Car:

#     def start(self):
#         print(self.brand, self.model, "is starting")
# ```

# ElectricCar:

# ```python
# def start(self):
#     print(self.brand, self.model,
#           "starts silently using electric power")
# ```

# SportsCar:

# ```python
# def start(self):
#     print(self.brand, self.model,
#           "starts with a powerful engine sound")
# ```

# All three methods have the same name:

# ```text
# start()
# ```

# But the child classes provide their **own implementation**.

# That's **Method Overriding**.
