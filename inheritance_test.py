class Animal():
    def __init__(self,name):
        self.name = name 


    def bark(self):
        print(f"The {self.name} is barking")



class Dog(Animal):
    def eat(self):
        print(f"{self.name} is eating")


dog = Dog("Bholu")

dog.bark()

dog.eat()
