from random import randint
from btree import BinaryTree

def main():
    myTree = BinaryTree()
    myTree.printInorder()
    for _ in range(1000):
        value = randint(0,20)
        myTree.insert(value)
    print("height: ", myTree.height(), myTree.root.left.height(), myTree.root.right.height())
    print(myTree.isBalanced())
    myTree.printInorder()
    myTree.find(12)
    myTree.find(200)

if __name__ == "__main__":
    main()
