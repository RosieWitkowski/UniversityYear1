class BankAccount():
    def __init__(self, accountNumber, balance):
        self.__accountNumber = accountNumber 
        self.__balance = balance

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

class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, balance):
        super().__init__(accountNumber, balance)

    def addInterest(self, interestRate: float):
        self._BankAccount__balance += (self._BankAccount__balance * (interestRate / 100) )
        return self._BankAccount__balance
    

JohnSmith = SavingsAccount("147148", 50)
JohnSmith.deposit(100)
bal = JohnSmith.getBalance()
print(f"Balance for JohnSmith: £{bal:.2f}")
JohnSmith.addInterest(10)
bal = JohnSmith.getBalance()
print(f"Balance for JohnSmith: £{bal:.2f}")