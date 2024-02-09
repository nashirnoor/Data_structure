class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self,val):
        self.top = Node(val)
        self.height = 1

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        self.top = self.top.next
         






a1 = Stack(20)
a1.push(44)
a1.push(26)
a1.pop()
a1.print()

