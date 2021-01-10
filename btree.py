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
        elif currNode == None:
            return self.height(self.root)
        else:
            leftChild = currNode.getLeftChild()
            rightChild = currNode.getRightChild()
            if leftChild == None:
                leftChildHeight = 0
            else:
                leftChildHeight = leftChild.height()
            if rightChild == None:
                rightChildHeight = 0
            else:
                rightChildHeight = rightChild.height()
            return 1 + max(leftChildHeight, rightChildHeight)


    def printPreorder(self):
        self.root.printPreorder()
    def printInorder(self):
        self.root.printInorder()
    def printPostorder(self):
        self.root.printPostorder()
    def isBalanced(self):
        return self.root.isBalanced()
    def find(self, value):
        return self.root.find(value)

    def __repr__(self):
        return repr(self.root)
