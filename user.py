class User:
    def __init__(self,name,email,balance=0):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: ${self.account_balance}")
    
    def make_deposit(self,amount):
        self.account_balance += amount

    def transfer_money(self,other_user,amount):
        self.account_balance-=amount
        other_user.account_balance+=amount
        print(self.name,"'s account balance: $",self.account_balance)
        print(other_user.name,"'s account balance: $",other_user.account_balance)

Jeff = User("Jeff","jeff@email.com")
Bob = User("Bob","bob@email.com")
Jenn = User("Jenn","jenn@email.com")

#have the first user make 3 deposits and 1 withdrawal
Jeff.make_deposit(25)
Jeff.make_deposit(50)
Jeff.make_deposit(25)
Jeff.make_withdrawal(30)
print("Jeff's account balance: $", Jeff.account_balance)

#Have the second user make 2 deposits and 2 withdrawals 
Bob.make_deposit(50)
Bob.make_deposit(25)
Bob.make_withdrawal(10)
Bob.make_withdrawal(15)
print("Bob's account balance: $",Bob.account_balance)

#Have the third user make 1 deposits and 3 withdrawals
Jenn.make_deposit(120)
Jenn.make_withdrawal(15)
Jenn.make_withdrawal(25)
Jenn.make_withdrawal(8)
print("Jenn's account balance: $",Jenn.account_balance)

#Add a transfer_money method; have the first user transfer money to the third user
Jeff.transfer_money(Jenn,30)