class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("No data")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("No data")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("data is present")


    

a1 = LinkedList()
a1.insert(88)
a1.add_after(12,88)
a1.add_after(11,12)

a1.print()