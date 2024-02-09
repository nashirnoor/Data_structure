class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length+=1

    def pop(self):
        if self.top is None:
            return
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length-=1


a1 = Stack(20)
a1.push(44)
a1.push(26)
a1.pop()
a1.print()

