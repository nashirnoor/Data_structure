class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("no dat")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def reverse(self):
        if self.head is None:
            print("no dat")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref 
            while n.pref is not None:
                print(n.data,end="")
                n = n.pref
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node


l1 = LinkedList()
l1.insert('F')
l1.insert('E')
l1.insert('D')
l1.insert('C')
l1.insert('B')
l1.insert('A')
l1.reverse()
l1.print()