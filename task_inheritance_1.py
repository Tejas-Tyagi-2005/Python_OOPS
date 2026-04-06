# TASK - Inheritance Practice 1
#
# Create a parent class called Vehicle with:
#   - Property: brand
#   - Method: start() -> prints "Vehicle started"
#
# Create a child class called Car that inherits from Vehicle with:
#   - Its own method: honk() -> prints "{brand} goes beep beep!"
#
# Create 1 Car object, call start() and honk() on it.

class Vehicle():
    def __init__(self , brand):
        self.brand = brand 


    def start(self):
        print(f"The vehicle started ")

class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} goes beep beep !")



gaadi = Car("Maserati")

gaadi.start()

gaadi.honk()
