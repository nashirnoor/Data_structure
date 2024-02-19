class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def search(self,val):
        if self.key == val:
            print("Value found")
            return
        if self.key > val:
            if self.lchild:
                self.lchild.search(val)
            else:
                print("Value not found")
        else:
            if self.rchild:
                self.rchild.search(val)
            else:
                print("VAlue not found")

        



root = BST(90)
arr = [7,34,87,143,12,1,90]
for i in arr:
    root.insert(i)

root.search(87)

