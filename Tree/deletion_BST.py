class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

        elif data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def inorder(self):
            if self.lchild:
                self.lchild.inorder()
            print(self.key,end=" ")
            if self.rchild:
                self.rchild.inorder()

    def delete(self,data):
        if self.key is None:
            print("No data in tree")
            return self
        if data < self.key:
            if self.lchild:
               self.lchild = self.lchild.delete(data)
        elif data > self.key:
            if self.rchild:
               self.rchild = self.rchild.delete(data)
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)

        return self 



root = BST(None)
arr = [4,88,66,23,133,87,90]
for i in arr:
    root.insert(i)

root.inorder()
print()
root.delete(7)
root.inorder()

