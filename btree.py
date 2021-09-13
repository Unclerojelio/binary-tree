from node import Node

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value, currNode=None):
        if self.root == None:
            self.root = Node(value)
            self.root.incrementCount()
        else:
            self.root.insert(Node(value))

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
        return self.root.find(value)

    def invert(self):
        if self.root != None:
            self.root.swap()

    def __repr__(self):
        return repr(self.root)
