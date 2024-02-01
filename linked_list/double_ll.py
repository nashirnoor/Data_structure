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
            print("No data")
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
    

            


