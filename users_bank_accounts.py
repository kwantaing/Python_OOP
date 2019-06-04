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


class User:
    def __init__(self,name,email,balance=0):
        self.name = name
        self.email = email
        self.account =BankAccount(int_rate = 0.02, balance=0)
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: ${self.account.balance}")
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def transfer_money(self,other_user,amount):
        self.account.balance-=amount
        other_user.account.balance+=amount
        print(self.name,"'s account balance: $",self.account.balance)
        print(other_user.name,"'s account balance: $",other_user.account.balance)
        return self

James = User("James","james@email.com")
James.make_deposit(40)  #James.account.Deposit(40) accomplishes the same thing
James.account.display_account_info()
