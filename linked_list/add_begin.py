class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None



class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("Linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        new_data = Node(data)
        new_data.ref = self.head
        self.head = new_data




a1 = LinkedList()
a1.add_begin(20)
a1.add_begin(99)
a1.print()