class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        n =self.head
        while n is not None:
            print(n.data)
            n = n.ref

    def insert(self,data):
        if self.head is None:
           new_node = Node(data)
           self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref 
            n.ref = new_node

    def delete_first(self):
        self.head = self.head.ref 



a1 = LinkedList()
a1.insert(10)
a1.add_end(12)
a1.add_end(21)
a1.add_end(99)
a1.delete_first()
a1.print()