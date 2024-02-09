class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self,val):
        new_node = Node(val)
        self.first = new_node
        self.last =  new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next

    def enqueue(self,val):
        new_node = Node(val)
        self.last.next = new_node
        self.last = new_node
        self.length +=1

a1 = Queue(10)
a1.enqueue(33)
a1.enqueue(99)
a1.print()