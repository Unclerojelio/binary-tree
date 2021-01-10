#python3 -m unittest btree_test

import unittest
from btree import BinaryTree

class TestTree(unittest.TestCase):

    def testCreate(self):
        myTree = BinaryTree()
        self.assertIsNone(myTree.root)

    def testInsert(self):
        myTree = BinaryTree()
        myTree.insert(2)
        self.assertEqual(myTree.root.getValue(), 2)

    def testHeight(self):
        myTree = BinaryTree()
        self.assertEqual(myTree.height(), 0)
        myTree.insert(2)
        self.assertEqual(myTree.height(), 1)
        myTree.insert(1)
        self.assertEqual(myTree.height(), 2)
        myTree.insert(3)
        self.assertEqual(myTree.height(), 2)
        myTree.insert(4)
        self.assertEqual(myTree.height(), 3)

    def testIsBalanced(self):
        myTree = BinaryTree()
        self.assertTrue(myTree.isBalanced())
        myTree.insert(2)
        self.assertTrue(myTree.isBalanced())
        myTree.insert(1)
        self.assertTrue(myTree.isBalanced())
        myTree.insert(3)
        self.assertTrue(myTree.isBalanced())
        myTree.insert(4)
        self.assertTrue(myTree.isBalanced())
        myTree.insert(5)
        self.assertFalse(myTree.isBalanced())
