# TASK - Abstraction Practice 1
#
# Import ABC and abstractmethod
#
# Create an abstract class called Vehicle with:
#   - Abstract method: move()
#
# Create 2 child classes: Car and Boat
#   - Car  -> move() prints "Car drives on road"
#   - Boat -> move() prints "Boat sails on water"
#
# Create 1 object of each and call move() on both.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"Car drives on road ")

class Boat(Vehicle):
        def move(self):
            print(f"Boat sails on water")


pinku = Car()

pinku.move()

golu = Boat()

golu.move()

