class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.count = 0
        if value != None:
            self.count = 1
        self.left = None
        self.right = None
        self.parent = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getCount(self):
        return self.count

    def incrementCount(self):
        self.count += 1

    def getParent(self):
        return self.parent

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

    def insert(self, value):
        if self.value == None:
            self.value = value
            self.count = 1
        elif self.value == value:
            self.count += 1
        elif self.value > value:
            if self.left == None:
                self.left = Node(value)
                self.left.count = 1
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
                self.right.count = 1
                self.right.parent = self
            else:
                self.right.insert(value)

    def replace_node_in_parent(self, new_value = None):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = new_value
            else:
                self.parent.right = new_value
        if new_value:
            new_value.parent = self.parent

    def delete(self, value):
        if value < self.value:
            self.left.delete(value)
            return
        if value > self.value:
            self.right.delete(value)
            return
        if self.left and self.right:
            successor = self.right.find_min()
            self.value = successor.value
            self.count = successor.count
            successor.delete(value)
        elif self.left:
            self.replace_node_in_parent(self.left)
        elif self.right:
            self.replace_node_in_parent(self.right)
        else:
            self.replace_node_in_parent(None)

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

    def count_children(self):
        if self.left and self.right:
            return 2 + self.left.count_children() + self.right.count_children()
        elif self.left:
            return 1 + self.left.count_children()
        elif self.right:
            return 1 + self.right.count_children()
        else:
            return 0
