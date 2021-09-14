class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.count = 0
        self.left = None
        self.right = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getCount(self):
        return self.count

    def incrementCount(self):
        self.count += 1

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def addLeftChild(self, n):
        self.left = n

    def addRightChild(self, n):
        self.right = n

    def __repr__(self):
        temp = (self.value, self.count, self.left, self.right)
        return str(temp)

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
                self.left.count = 1
            else:
                self.left.insert(newNode)
        else:
            if self.right == None:
                self.right = newNode
                self.right.count = 1
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
            return None
        elif self.value == value:
            return self.count
        elif value < self.value:
            if self.left != None:
                return self.left.find(value)
            else:
                return None
        else:
            if self.right != None:
                return self.right.find(value)
            else:
                return None

    def swap(self):
        temp = self.left
        self.left = self.right
        self.right = temp
        if self.left != None:
            self.left.swap()
        if self.right != None:
            self.right.swap()

    def total(self):
        if self.left == None:
            leftCount = 0
        else:
            leftCount = self.left.total()
        if self.right == None:
            rightCount = 0
        else:
            rightCount = self.right.total()
        return self.count + leftCount + rightCount

    def find_min(self):
        if self.left == None:
            return self
        else:
            return self.left.find_min()
