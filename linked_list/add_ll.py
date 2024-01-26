class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("No data in head!!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref


    def add_being(self,data):
        add_val = Node(data)
        add_val.ref = self.head
        self.head = add_val

    def add_end(self,data):
        add_val = Node(data)
        if self.head is None:
            self.head = add_val
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = add_val


    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("no data")
        else:
            add_val = Node(data)
            add_val.ref = n.ref
            n.ref = add_val 

                 
d1 = LinkedList()
d1.add_being(12)
d1.add_being(123)
d1.add_end(88)
d1.add_after(666,12)

d1.print()