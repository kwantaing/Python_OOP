class User:
    def __init__(self,name,email,balance=0):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: ${self.account_balance}")
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance-=amount
        other_user.account_balance+=amount
        print(self.name,"'s account balance: $",self.account_balance)
        print(other_user.name,"'s account balance: $",other_user.account_balance)
        return self

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
