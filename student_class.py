class Student():
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def result(self):
        if self.marks >= 50:
            print("Pass")    
        else:
            print("Fail")    



student_1 = Student("pinku",55)     

print(student_1.marks)

student_1.result()


    


