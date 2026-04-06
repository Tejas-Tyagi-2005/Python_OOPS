class Phone():
    def __init__(self , battery):
        self.__battery = battery 

    def get_battery(self):
        print(f"Battery : {self.__battery}")


    def charge(self,amount):
        if self.__battery + amount <= 100:
            self.__battery = self.__battery + amount 
            print(f"The battery is now {self.__battery}")
        else:
            print(f"The battery is already full ")

ph1 = Phone(50)

ph1.get_battery()

ph1.charge(40)

