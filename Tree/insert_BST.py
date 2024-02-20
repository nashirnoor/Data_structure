class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key>data:
            if  self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if  self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is Present")
            return 
        
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found!!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found!!")

root = BST(10)
list1 = [5,3,19,22,77,23]
for i in list1:
    root.insert(i)
root.search(77)
