from node import Node


class BinaryTree(object):
    def __init__(self):
        self.root = None
    def insert(self, value, currNode=None):
        if self.root == None and currNode == None:
            currNode = Node(value)
            self.root = currNode
        elif currNode == None:
            self.insert(value, self.root)
        elif currNode.value == value:
            currNode.incrementCount()
        elif currNode.value > value:
            if currNode.getLeftChild() == None:
                currNode.addLeftChild(Node(value))
            else:
                self.insert(value, currNode.getLeftChild())
        elif currNode.value < value:
            if currNode.getRightChild() == None:
                currNode.addRightChild(Node(value))
            else:
                self.insert(value, currNode.getRightChild())

    def height(self, currNode=None):
        if self.root == None:
            return 0
        else:
            return self.root.height()

    def isBalanced(self, currNode=None):
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
