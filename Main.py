#Assignment 1: Design Your Own Class! 🏗️

# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.model} is calling {number}... 📞")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Inheritance: Specialized class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    # Overriding method
    def info(self):
        print(f"Smartwatch Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Strap Color: {self.strap_color}")

# Creating objects
phone = Smartphone("Samsung", "Galaxy S22", 128)
watch = Smartwatch("Apple", "Watch Series 8", 32, "Black")

phone.info()
phone.call("+123456789")
print("\n")
watch.info()
watch.call("+987654321")

# Activity 2: Polymorphism Challenge! 🎭

# Base class
class Vehicle:
    def move(self):
        print("Moving...")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

# Using Polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

