# Task: Code based on the given UML diagram (UML1.png)
class BankAccount():
    def __init__(self):
        self.__accountNumber = None 
        self.__balance = 0 

    def deposit(self, amount: float):
        self.__balance += amount 
    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount 
            print(f"{amount} withdrawn successfully")
            return True 
        print(f"Unable to withdraw {amount}")
        return False  
    def getBalance(self):
        return self.__balance 

JohnSmith = BankAccount()
JohnSmith.deposit(20)
JohnSmith.withdraw(50)
JohnSmith.deposit(90)
JohnSmith.withdraw(10)
bal = JohnSmith.getBalance()
print(f"Balance for JohnSmith: £{bal}")