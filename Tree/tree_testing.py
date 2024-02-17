class Tree:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None


root = Tree(10)


root.lchild = Tree(17)
root.rchild = Tree(66)
print(root.key)
print(root.lchild)
print(root.rchild)
print(root.lchild.key)
print(root.lchild.rchild)
print(root.lchild.lchild)
print(root.rchild.key)
print(root.rchild.rchild)
print(root.rchild.lchild)



