class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age 


    def bite(self):
        print(f"{self.name} bit you !")


dog1 = dog("pinku",8) 

dog2 = dog("bholu",2)
dog2.bite()

print(dog1.name)

print(dog2.age)


