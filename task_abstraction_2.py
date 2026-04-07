# TASK - Abstraction Practice 2
#
# Import ABC and abstractmethod
#
# Create an abstract class called Appliance with:
#   - Abstract method: turn_on()
#
# Create 3 child classes: Fan, AC, Washing Machine
#   - Fan            -> turn_on() prints "Fan is spinning"
#   - AC             -> turn_on() prints "AC is cooling"
#   - WashingMachine -> turn_on() prints "WashingMachine is washing"
#
# Create a list with one object of each, loop and call turn_on() on all.


from abc import ABC , abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print(f"The fan is spinning")

class AC(Appliance):
    def turn_on(self):
        print(f"The AC is cooling ")

class WashingMachine(Appliance):
    def turn_on(self):
        print(f"The washing machine is washing")


pankha = Fan()

pankha.turn_on()

Hitachi = AC()
Hitachi.turn_on()

Bosch = WashingMachine()
Bosch.turn_on()



    
