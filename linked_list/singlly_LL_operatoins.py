class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("No data available!!")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_begin(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_data = Node(data)
            new_data.ref = self.head
            self.head = new_data

    def add_end(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = Node(data)

    def insert_after(self,data,x):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n is not None:
               if n.data == x:
                   break
               n = n.ref
            if n is None:
                print("No data")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def insert_before(self,data,x):
        if self.head is None:
            return
        if self.head.data == x:
            new_node  = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n is None:
                print("Value not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("No data")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("NO")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_value(self,x):
        if self.head is None:
            print("nnnnn")
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("not data")
            else:
                n.ref = n.ref.ref
   

a1 = LinkedList()
a1.add_begin(20)
a1.add_begin(12)
a1.add_begin(101)
a1.add_end(67)
a1.insert_after(43,20)
a1.insert_before(44,101)
a1.delete_value(20)
a1.print()