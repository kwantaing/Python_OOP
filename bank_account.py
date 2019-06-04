class BankAccount:
    def __init__(self,int_rate, balance):
        self.int_rate = int_rate
        self.balance  = balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if(self.balance>=amount):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self

    def display_account_info(self):
        print("Balance: $",self.balance)

    def yield_interest(self):
        self.balance+=(self.balance*self.int_rate)
        print("Balance: $",self.balance)
        return self


A = BankAccount(0.05,1000)
B = BankAccount(0.08,500)

#make 3 deposits and 1 withdrawal, calc interest and display the info
A.deposit(100).deposit(50).deposit(150).withdraw(200).yield_interest()

#make 2 deposits and 4 withdrawal, calc interest and display
B.deposit(500).deposit(100).withdraw(25).withdraw(30).withdraw(50).withdraw(10).yield_interest()
