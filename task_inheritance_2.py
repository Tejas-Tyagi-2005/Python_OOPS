# TASK - Inheritance Practice 2
#
# Create a parent class called Person with:
#   - Properties: name, age
#   - Method: introduce() -> prints "Hi I am {name} and I am {age} years old"
#
# Create a child class called Student that inherits from Person with:
#   - Its own property: marks
#   - Its own method: result() -> prints "Pass" if marks >= 50 else "Fail"
#
# Create 1 Student object, call introduce() and result() on it.

class Person():
    def __init__(self , name , age):
        self.name = name
        self.age = age 

    def introduce(self):
        print(f"Hello im {self.name} and im {self.age} years old ")


class Student(Person):
    def __init__(self,marks,name,age):
        super().__init__(name,age)
        self.marks = marks 

    def result(self):
        if self.marks >= 50 :
            print("Pass")
        else:
            print("Fail")    


uno = Student(90,"Tejas",20)

uno.introduce()

uno.result()
