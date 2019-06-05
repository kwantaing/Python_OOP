class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
    	self.head = None

    def add_to_front(self,val):         # added this line, takes a value
        new_node = SLNode(val)          # create a new instance of our Node class using the given value
        current_head = self.head        # save the current head in a variable
        new_node.next = current_head    # SET the new node's next TO the list's current head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head              # a pointer to the list's first node
        while (runner != None):         # iterating while runner is a node and not None
            print(runner.value)         # print the current node's value
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:           #if the list is empty
            self.add_to_front(val)      #run the add_to_front method
            return self                 #make sure end function if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node          #increment the runner to next node on list
        return self                     #return self to allow for chaining
    
    def remove_from_back(self):
        if self.head == None:
            return "empty list"
        runner = self.head
        while(runner.next != None):
            temp = runner               #create a variable to hope current runner position
            runner = runner.next        #move runner to next position
            if(runner.next == None):    #if the runner is the last in the list
                temp.next= None         #remove that runner from list using reference of temp
                return self
        return self
     
    def remove_from_front(self):
        self.head = self.head.next
        return self

    def remove_val(self,val):
        runner = self.head
        if(runner.value == val):
            self.remove_from_front()
            return self
        while(runner.next != None):      #if value is in middle
            temp = runner               #temp to hold onto current runner position
            runner = runner.next        #move runner to next position
            if(runner.value == val):    # if the value is matching,
                temp.next = runner.next #using the temp.next to reference current runner position
                return self                 ##can establish .next link to after runner.next
        if(runner.value == val):            ##effectively unlinks the node with that value with everything else!
            self.remove_from_back()
        return self

    def find_length_of_SLL(self):
        length = 0
        if(self.head):
            length = 1
            runner = self.head
            while(runner.next != None):
                runner = runner.next
                length+=1
            return length
        print("Empty Linked List")
        return self

    def insert_at(self,val,n):
        if(n == 1):
            self.add_to_front(val)
            return self
        if(n == self.find_length_of_SLL):
            print("back")
            self.add_to_back(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        index = 1
        while(runner.next != None):
            temp = runner
            runner = runner.next
            index += 1
            if(index == n):
                temp.next = new_node
                new_node.next = runner
                return self
        return self
        




        

# my_list = SList()
# my_list.add_to_front("are").add_to_front("linked lists").add_to_back("fun!").print_values()

# my_list.remove_from_front().print_values()
# my_list.remove_from_back().remove_from_back().print_values()
# my_list2 = SList()
# my_list2.add_to_front(4).add_to_front(5).add_to_front(6).add_to_front(7).print_values()
# my_list2.remove_from_back().remove_from_front().print_values()

# my_list2.remove_val(7).print_values()  #remove from front with value in front
# my_list2.remove_val(6).print_values()  #remove from front with value in middle
# my_list2.remove_val(4).print_values()  #remove from front with value in back

# my_list.remove_val("linked lists").print_values()
# my_list.remove_val("are").print_values()
# my_list.remove_val("fun!").print_values()
my_list3 = SList()
my_list3.add_to_front(3).add_to_front(4).add_to_front(6).add_to_front(7).print_values()
my_list3.find_length_of_SLL()
my_list3.insert_at(5,1).print_values()
# my_list3.print_values()
# my_list3.add_to_back(5).print_values()