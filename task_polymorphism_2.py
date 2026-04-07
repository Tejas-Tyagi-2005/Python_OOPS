# TASK - Polymorphism Practice 2
#
# Create 3 classes: Car, Bike, Truck
# Each class has one method: fuel_type()
#   - Car   -> prints "Car runs on Petrol"
#   - Bike  -> prints "Bike runs on Diesel"
#   - Truck -> prints "Truck runs on CNG"
#
# Create a list with one object of each class.
# Loop through the list and call fuel_type() on each.

class Car():
    def fuel_type(self):
        print(f"Car runs on petrol ")
class Bike():
    def fuel_type(self):
        print(f"Bike runs on diesel")
class Truck():
    def fuel_type(self):
        print(f"Truck runs on CNG")
vehicles = [Car(),Bike(),Truck()]
for vehicle in vehicles:
    vehicle.fuel_type()                        