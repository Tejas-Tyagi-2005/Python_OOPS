class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner 
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"New balance : {self.balance} ")

    def withdraw(self,amount):
        self.balance = self.balance - amount 
        print(f"New balance ")        

acc1 = BankAccount("Tejas", 7000)

acc1.deposit(1000)