class Student():
    def __init__(self,marks):
        self.__marks = marks 


    def view_marks(self):
        print(f"Iris scan mismatch , you are not authorized to view marks ")    

    def update_marks(self , marks):
        if marks >= 0 and marks <= 100 :
            self.__marks = marks 
            print(f"The new marks are {self.__marks}")
        else:
            print("Invalid marks entered ")


Tejas = Student(50)

Tejas.view_marks()

Tejas.update_marks(70)