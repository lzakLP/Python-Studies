# ACTIVITY: MODELING VEHICLES WITH INHERITANCE
#
# Develop a Python program that represents vehicles using classes,
# attributes, methods, inheritance, and method overriding.
#
# The program must:
# 1. Define a parent class called Vehicle with the attributes
#    brand, model, year, and speed. The initial speed must be zero.
# 2. Implement the following methods in Vehicle:
#    - accelerate(): increase the speed by a given amount.
#    - brake(): decrease the speed by a given amount.
#    - status(): return the vehicle's attributes and current speed.
# 3. Define a Car class that inherits from Vehicle:
#    - Add a power attribute.
#    - Override accelerate() to increase the speed by the given
#      increment plus the power value, using the exercise's simplified rule.
# 4. Define a Bicycle class that inherits from Vehicle:
#    - Add a bicycle_type attribute.
#    - Override status() to include the bicycle type.
# 5. Use super().__init__() in both child classes to initialize
#    the attributes inherited from Vehicle.
# 6. Create a car and a bicycle, accelerate them, and display their status.
#
# This activity practices object-oriented programming, constructors,
# inheritance, and method overriding.
#
# Write your code below:

class Vehicle:
    # Initialize the vehicle's attributes.
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    # Increase the current speed.
    def accelerate(self, increment):
        self.speed += increment

    # Decrease the current speed.
    def brake(self, decrement):
        self.speed -= decrement

    # Return the vehicle's information and current speed.
    def status(self):
        return (
            f"Brand: {self.brand}, Model: {self.model}, "
            f"Year: {self.year}, Speed: {self.speed} km/h"
        )


class Car(Vehicle):
    # Initialize inherited attributes and add the car's power.
    def __init__(self, brand, model, year, power):
        super().__init__(brand, model, year)
        self.power = power

    # Override acceleration using the exercise's simplified rule.
    def accelerate(self, increment):
        self.speed += increment + self.power


class Bicycle(Vehicle):
    # Initialize inherited attributes and add the bicycle type.
    def __init__(self, brand, model, year, bicycle_type):
        super().__init__(brand, model, year)
        self.bicycle_type = bicycle_type

    # Override the status method to include the bicycle type.
    def status(self):
        return (
            f"Brand: {self.brand}, Model: {self.model}, "
            f"Year: {self.year}, Type: {self.bicycle_type}, "
            f"Speed: {self.speed} km/h"
        )


# Create the vehicle objects.
car1 = Car("Toyota", "Corolla", 2022, 150)
bicycle1 = Bicycle("Trek", "Mountain Bike", 2021, "MTB")

# Accelerate the vehicles.
car1.accelerate(50)
bicycle1.accelerate(20)

# Display the status of each vehicle.
print("Car Status:")
print(car1.status())

print("\nBicycle Status:")
print(bicycle1.status())
