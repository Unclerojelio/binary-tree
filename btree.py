from node import Node

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.root.incrementCount()
        else:
            self.root.insert(value)

    def delete(self, value):
        if self.root:
            if self.root.getLeftChild() == None and \
            self.root.getRightChild() == None and \
            self.root.getValue() == value:
                self.root = None
            else:
                self.root.delete(value)

    def size(self):
        if self.root == None:
            return 0
        else:
            return 1 + self.root.count_children()

    def height(self):
        if self.root == None:
            return 0
        else:
            return self.root.height()

    def isBalanced(self):
        if self.root == None:
            return True
        else:
            return self.root.isBalanced()

    def printPreorder(self):
        if self.root != None:
            self.root.printPreorder()

    def printInorder(self):
        if self.root != None:
            self.root.printInorder()

    def printPostorder(self):
        if self.root != None:
            self.root.printPostorder()

    def find(self, value):
        if self.root != None:
            return self.root.find(value)

    def invert(self):
        if self.root != None:
            self.root.swap()

    def total(self):
        if self.root == None:
            return 0
        else:
            return self.root.total()

    def __repr__(self):
        return repr(self.root)
