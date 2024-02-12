import collections 
import queue
sam = [1,3,4,4,4,4,42,2,2,2,7,8,9,7,7]
a = collections.deque()
b = queue.LifoQueue()
a.append(19)
print(a)
b.put(88)
b.put(99)
b.get()
print(b.get())


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        self.top = Node(value)
        self.length =1

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.top =  new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        temp = self.top
        self.top = self.top.next
        # temp.next = None
        self.length-=1
        return temp

a1 = Stack(29)
a1.push(77)
a1.push(55)
a1.push(33)
a1.pop()
a1.pop()

a1.print()
        
