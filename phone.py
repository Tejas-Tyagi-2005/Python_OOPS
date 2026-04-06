class Phone():
    def __init__(self, brand, battery):
        self.brand = brand 
        self.battery = battery 

    def make_call(self,minutes):
        self.battery = self.battery - minutes * 2
        print(f"Battery left :{self.battery}")

    def charge(self):
        self.battery = 100
        print(f"Battery is {self.battery}")   


ph1 = Phone("Apple" , 50)

ph2 = Phone("Samsung" , 100)

ph1.make_call(10)

ph1.charge()


