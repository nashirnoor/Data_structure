class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if  data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        elif data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
        else:
            print("Duplicate val")
            return

    def search(self,data):
        if self.key == data:
            print("Data is available")
            return
        if self.key > data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("No data available")
        else:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Data is not available")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()


root = BST(None)
arr = [88,34,21,65,1,3,5,18,41,101,175,255,103,65,103]


for i in arr:
    root.insert(i)

root.search(18)
print("Preorder:",end=" ")
root.preorder()
print()
print("Postorder:",end=" ")
root.postorder()
print()
print("Inorder:",end=" ")
root.inorder()


