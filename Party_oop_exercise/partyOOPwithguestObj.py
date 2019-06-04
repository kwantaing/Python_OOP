class Party:
    def __init__(self,cap):
        self.capacity = cap
        self.guests = []
    # def introduceGuest(self,name,age,gender):
    #     newGuest = Guest(self,name,age,gender)
    #     self.welcomeguest(newGuest)
    def welcomeguest(self,guest):
        if(len(self.guests)<self.capacity):
            self.guests.append(guest)
            print(self.guests)
        else:
            print("Party is full")
    def bootguest(self,guestname):
        for i in range(len(self.guests)):
            if(guestname == self.guests[i].name):
                self.guests.pop(i)


class Guest:
    def __init__(self,name="Jeff",age=69,gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender

newParty= Party(50)
print(newParty.capacity)
newguest = Guest("Bob",21,"Male")
print(newguest.name)
newParty.welcomeguest(newguest)