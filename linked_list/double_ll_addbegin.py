class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("No data availa")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def reverse(self):
        if self.head is None:
            print("No data")

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref

            while n is not None:
                print(n.data)
                n = n.pref

    def add_after(self,data,x):
        if self.head is None:
            print("no data available!!")

        else:
            n = self.head
            while n is not None:
               if x==n.data:
                 break
               n = n.nref
            
            if n is None:
                print("NOOO")
            else:
                new_node = Node(data)
                new_node.nref = n.ref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                
                n.nref = new_node

        



