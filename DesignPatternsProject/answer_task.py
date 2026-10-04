# Data Layer
class UserData:
    def get_user(self):
        return "Piro"

# Business Layer
class UserService:
    def __init__(self):
        self.data = UserData()

    def get_user_name(self):
        name = self.data.get_user()
        return "Hello " + name

# Presentation Layer
class UserUI:
    def __init__(self):
        self.service = UserService()

    def show_user(self):
        message = self.service.get_user_name()
        print(message)

# Run the program
ui = UserUI()
ui.show_user()

# Factory Pattern
class Car:
    def drive(self):
        print("Car is driving")

class Bike:
    def drive(self):
        print("Bike is driving")

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()

        if vehicle_type == "bike":
            return Bike()

# Create vehicles
factory = VehicleFactory()

car = factory.create_vehicle("car")
car.drive()

bike = factory.create_vehicle("bike")
bike.drive()

# Strategy Pattern
class Add:
    def calculate(self, a, b):
        return a + b

class Multiply:
    def calculate(self, a, b):
        return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.calculate(a, b)

# Use Add strategy
calculator = Calculator(Add())
print("Addition:", calculator.calculate(5, 3))

# Use Multiply strategy
calculator = Calculator(Multiply())
print("Multiplication:", calculator.calculate(5, 3))