from random import randint
from btree import BinaryTree

def main():
    myTree = BinaryTree()
    myTree.printInorder()
    for _ in range(1000):
        value = randint(0,20)
        myTree.insert(value)
    print("height: ", myTree.height(), myTree.root.left.height(), myTree.root.right.height())
    print("size: {}".format(myTree.size()))
    print("isBalanced: {}".format(myTree.isBalanced()))
    print("isBST: {}".format(myTree.isBST()))
    myTree.printInorder()
    print (myTree.find(12))
    print (myTree.find(200))
    myTree.invert()
    myTree.printInorder()

    # myTree = BinaryTree()
    # print(myTree)
    # myTree.insert(2)
    # myTree.insert(3)
    # myTree.insert(1)
    # myTree.printPostorder()
    # print(myTree)
    # myTree.invert()
    # print(myTree)

if __name__ == "__main__":
    main()
