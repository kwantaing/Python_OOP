class Party:
    def __init__(self,cap):
        self.capacity = cap
        self.guests = []
    def welcomeguest(self,guest_name):
        if(len(self.guests)<self.capacity):
            self.guests.append(guest_name)
            print(self.guests)
        else:
            print("Party is full")
    def bootguest(self,guest_name):
        for i in range(len(self.guests)):
            if(guest_name == self.guests[i]):
                self.guests.pop(i)
    def current_size(self):
        return len(self.guests)
    def changeSize(self,newSize):
        self.capacity = newSize
        while(self.current_size> self.capacity):
            self.guests.pop()
        

Lit = Party(10)
Lit.welcomeguest("John")
Lit.welcomeguest("Brian")
Lit.welcomeguest("Bill")
Lit.welcomeguest("Nye")
Lit.welcomeguest("David")
Lit.welcomeguest("Jill")
Lit.welcomeguest("Jack")
Lit.welcomeguest("Swift")

print(Lit.guests)
print(Lit.guests)

