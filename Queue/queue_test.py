class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self,data):
        new_node = Node(data)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.data)
            temp = temp.next

a1 = Queue(99)
a1.print()
