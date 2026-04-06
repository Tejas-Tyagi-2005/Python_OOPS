class car():
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed


    def describe(self):
        print(f"{self.brand} is going at {self.speed}") 


gaadi = car("BMW", 230)

toto = car("tirri" , 30)

gaadi.describe()

toto.describe()