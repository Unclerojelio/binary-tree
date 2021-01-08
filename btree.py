from node import Node


class BinaryTree(object):
    def __init__(self):
        self.root = Node()
    def insert(self, value):
        newNode = Node(value)
        self.root.insert(newNode)
    def printPreorder(self):
        self.root.printPreorder()
    def printInorder(self):
        self.root.printInorder()
    def printPostorder(self):
        self.root.printPostorder()
    def height(self):
        return self.root.height()
    def isBalanced(self):
        return self.root.isBalanced()
    def find(self, value):
        return self.root.find(value)
