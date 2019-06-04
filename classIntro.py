# class User:		# declare a class and give it name Usercopy
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance 


class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount


guido = User("Guideo van Rossum", "guido@python.com")
print(guido.name)
monty = User("Monty Python", "monty@python.com")
print(monty.email)
guido.make_deposit(100)
print(guido.account_balance)