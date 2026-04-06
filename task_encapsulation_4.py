# TASK - Encapsulation Practice 4
#
# Create a class called Employee with:
#   - Private property: __salary
#   - Method: get_salary()        -> prints the salary
#   - Method: raise_salary(amount)-> adds amount to salary ONLY if amount > 0
#                                    else prints "Invalid raise"
#
# Create 1 object, check salary, give valid raise, give invalid raise.

class Employee():
    def __init__(self,salary):
        self.__salary = salary


    def get_salary(self):
        print(f"The salary is {self.__salary}")

    def raise_salary(self,amount):
        if amount > 0 :
            self.__salary += amount 
            print(f"The new salary is {self.__salary}")
        else:
            print("Invalid amount ")            


Tejas = Employee(100)

Tejas.get_salary()

Tejas.raise_salary(50)