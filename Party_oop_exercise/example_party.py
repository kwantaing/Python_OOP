class Guest:
    def __init__(self,name,importance):
        self.name = name
        self.importance = importance
    def __repr__(self):
        return (f"Name: {self.name}, Importance: {importance}")

# class Party:    w/o object Guest

#     def __init__(self, capacity):
#         self.guests =[]
#         self.capacity = capacity
#     def current_size(self):
#         return len(self.guests)

#     def welcome_guest(self, guest_name):
#         #make sure we have the capacity
#         if(len(self.guests) == self.capacity):
#             print("sorry bro, no can do")
#         else:
#             #add name to guest
#             self.guests.append(guest_name)

#     def boot_guest(self, guest_name):
#         if guest_name in self.guests:
#             self.guests.remove(guest_name)
#         else:
#             print("Guest not found!")
class Party:    #w/ Object Guest

    def __init__(self, capacity):
        self.guests =[]
        self.capacity = capacity
    def current_size(self):
        return len(self.guests)

    def welcome_guest(self, guest_name):
        #make sure we have the capacity
        if(len(self.guests) == self.capacity):
            print("sorry bro, no can do")
        else:
            #add name to guest
            self.guests.append(guest_name)

    def boot_guest(self, guest_name):
        if guest_name in self.guests:
            self.guests.remove(guest_name)
        else:
            print("Guest not found!")


rager = Party(10)

rager.welcome_guest("Bill")
rager.welcome_guest("Cindy")
rager.welcome_guest("Dean")
rager.welcome_guest("Evelyn")
rager.welcome_guest("Fred")
rager.welcome_guest("Greg")
rager.welcome_guest("Hellen")
rager.welcome_guest("Ian")
rager.welcome_guest("Jill")
rager.welcome_guest("kylie")

rager.boot_guest("Jill")
print(rager.guests)

jeff = Guest("Jeff",5)