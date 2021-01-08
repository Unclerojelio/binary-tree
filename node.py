class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.count = 0
        self.left = None
        self.right = None

    def insert(self, newNode):
        if self.value == None:
            self.value = newNode.value
            self.count = 1
        elif newNode.value == self.value:
            self.count += 1
            return
        elif newNode.value < self.value:
            if self.left == None:
                self.left = newNode
                newNode.count = 1
            else:
                self.left.insert(newNode)
        else:
            if self.right == None:
                self.right = newNode
                newNode.count = 1
            else:
                self.right.insert(newNode)

 #   def balance(self):
 #       leftHeight = 0
 #       rightHeight = 0
 #       if self.left != None:
 #           leftHeight = self.left.height()
 #       if self.right != None:
 #           rightHeight = self.right.height()
 #       if leftHeight - rightHeight > 1:
 #           self.left.balance()
 #       elif rightHeight - leftHeight > 1:
 #           self.right.balance()


    def printPreorder(self):
        print(self.value, self.count)
        if self.left != None:
            self.left.printPreorder()
        if self.right != None:
            self.right.printPreorder()

    def printInorder(self):
        if self.left != None:
            self.left.printInorder()
        print(self.value , self.count)
        if self.right != None:
            self.right.printInorder()

    def printPostorder(self):
        if self.left != None:
            self.left.printPostorder()
        if self.right != None:
            self.right.printPostorder()
        print(self.value, self.count)

    def height(self):
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = self.left.height()
        if self.right != None:
            rightHeight = self.right.height()
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self):
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = self.left.height()
        if self.right != None:
            rightHeight = self.right.height()
        return abs(leftHeight - rightHeight) <= 1

    def find(self,value):
        if self.value == None:
            print("not found")
        elif self.value == value:
            print(self.count)
        elif value < self.value:
            if self.left != None:
                self.left.find(value)
            else:
                print("not found")
        else:
            if self.right != None:
                self.right.find(value)
            else:
                print("not found")
