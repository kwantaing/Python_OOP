class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # def print_values(self):
    #     if(self.head):
    #         runner = self.head              # a pointer to the list's first node
    #         print(self.head.value)
    #         runner = runner.next
    #     while (runner.next != None):         # iterating while runner is a node and not None
    #         print(runner.value)         # print the current node's value
    #         runner = runner.next
    #     return self
    def print_values(self):
        runner = self.head              # a pointer to the list's first node
        while (runner != None):         # iterating while runner is a node and not None
            print(runner.value)         # print the current node's value
            runner = runner.next
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

    #add new node
        #add to front(val)
    def add_to_front(self,val):
        new_node = Node(val)
        if(self.head==None):
            self.head = new_node
            self.tail = self.head
            return self
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
        return self

        #add to back(val)
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = Node(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        self.tail = new_node
        return self

        #insert new node between existing nodes
    def insert_at(self,val,n):
        if(n == 0):
            return "Invalid position 0 or less"
        if(n == 1):
            self.add_to_front(val)
            return self
        if(n > self.find_length_of_SLL()):
            print("Out of bounds")
            return self
        if(n == self.find_length_of_SLL()):
            print("back")
            self.add_to_back(val)
            return self
        new_node = Node(val)
        runner = self.head
        index = 1
        while(runner.next != None):
            temp = runner
            runner = runner.next
            index += 1
            if(index == n):
                temp.next = new_node
                new_node.next = runner
                new_node.prev = temp
                return self
        return self
    #delete existing node
        #remove from front
    def remove_from_front(self):
        self.head = self.head.next
        self.head.prev = None
        return self
    
    def remove_from_back(self):
        runner = self.head
        if self.head == None:
            return "empty list"
            runner = self.head
        while(runner.next != None):
                temp = runner
                runner = runner.next
        if(runner.next == None):
                temp.next = None
                runner.prev = None
                return self
        return self

    def remove_val(self,val):
        runner = self.head
        if(runner.value == val):
            self.remove_from_front()
            return self
        while(runner.next != None):
            before = runner
            runner = runner.next
            after = runner.next
            if(runner.value == val):
                after.prev = before
                before.next = after
                return self

DL = DoublyLinkedList()
DL.add_to_front(15).print_values().add_to_front(10).add_to_front("Hi").add_to_back("Bye").print_values()
DL.add_to_back(10).print_values()
DL.insert_at("Last",5).print_values()
DL.print_values()
DL.remove_from_front().print_values()
DL.remove_from_back().print_values()
DL.remove_val(15).print_values()