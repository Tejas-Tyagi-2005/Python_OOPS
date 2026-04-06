class Student():
    def __init__(self,marks):
        self.__marks = marks 

    def  get_marks(self):
        print(f"Marks are {self.__marks}")

    def   set_marks(self,marks):
        
        if input(self.__marks) >= 0 and self.__marks <= 100:
            print(f"Marks are {self.__marks}")


cole = Student(34)

cole.get_marks()

cole.set_marks()
           