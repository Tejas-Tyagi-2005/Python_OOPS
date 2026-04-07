# TASK - Inheritance Practice 4
#
# Create a parent class called Employee with:
#   - Properties: name, salary
#   - Method: work() -> prints "{name} is working"
#
# Create a child class called Manager that inherits from Employee with:
#   - Extra property: department
#   - Method: manage() -> prints "{name} is managing {department} department"
#
# Create 1 Manager object, call work() and manage() on it.


class Employee():
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary 

    def work(self):
        print(f"{self.name} is working ")



class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name , salary)
        self.department = department 

    def manage(self):
        print(f"{self.name} is managing {self.department}")    


m1 = Manager("Rohan", 15000,"sales")    

m1.work()

m1.manage()
