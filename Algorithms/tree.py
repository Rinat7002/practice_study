class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)



left = Tree(2)
right = Tree(3)

myTree = Tree(10, left, right)

# Sum of all elements of tree
def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

print(total(myTree))



