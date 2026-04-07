# TASK - Inheritance Practice 3
#
# Create a parent class called Animal with:
#   - Property: name
#   - Method: breathe() -> prints "{name} is breathing"
#
# Create a child class called Bird that inherits from Animal with:
#   - Extra property: wingspan
#   - Method: fly() -> prints "{name} flies with wingspan {wingspan}cm"
#
# Create 1 Bird object, call breathe() and fly() on it.

class Animal():
    def __init__(self , name):
        self.name = name 

    def breathe(self):
        print(f"{self.name} is breathing")


class Bird(Animal):
    def __init__(self,name,wingspan):
        super().__init__(name)
        self.wingspan = wingspan 


    def fly(self):
        print(f"{self.name} flies with {self.wingspan}cm")


pigin = Bird("fly_thing",5)

pigin.breathe()

pigin.fly()