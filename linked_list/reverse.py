class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.ref
        print()

    def addend(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = Node(data)

    def reverse(self):
        current = self.head
        nxt = None
        prev = None
        while(current):
            nxt = current.ref
            current.ref = prev
            prev = current
            current = nxt
        self.head = prev
        return self.head


a1 = LinkedList()
a1.addend(11)
a1.addend(17)
a1.addend(19)
a1.addend(17)
a1.print()
a1.reverse()
a1.print()