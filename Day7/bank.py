class Bank:
    def __init__(self,balance,acc):
        self.balance=balance
        self.acc=acc
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Total balance=",self.get_balance())
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("Total balance=",self.get_balance())
    
    def get_balance(self):
        return self.balance


acc1=Bank(10000,1256)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)
print(acc1.balance)
print(acc1.acc)
        