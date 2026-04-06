# TASK - Encapsulation Practice 3
#
# Create a class called Laptop with:
#   - Private property: __price
#   - Method: get_price()      -> prints the price
#   - Method: set_price(amount)-> updates price ONLY if amount > 0
#                                 else prints "Invalid price"
#
# Create 1 object, check price, set a valid price, set an invalid price.



class Laptop():
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        print(f"The price is {self.__price}")

    def set_price(self,amount):
        if amount > 0 :
            self.__price = amount
            print(f"The amount is {self.__price}")
        else:
            print(f"Invalid price")    


acer = Laptop(50000)

acer.get_price()

acer.set_price(20000)
