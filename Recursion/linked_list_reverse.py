class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.ref
        print()

    def addend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = Node(data)

    def reverse_recursive(self, current, prev):
        if current is None:
            self.head = prev
            return
        nxt = current.ref
        current.ref = prev
        self.reverse_recursive(nxt, current)

    def reverse(self):
        self.reverse_recursive(self.head, None)

a1 = LinkedList()
a1.addend(11)
a1.addend(17)
a1.addend(19)
a1.addend(17)

print("Original Linked List:")
a1.print()

print("\nReversed Linked List:")
a1.reverse()
a1.print()
