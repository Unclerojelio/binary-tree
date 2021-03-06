#python3 -m unittest btree_test

import unittest
import contextlib
import io
import sys
from random import randint
from btree import BinaryTree

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1
 
class TestTree(unittest.TestCase):

    def testCreate(self):
        myTree = BinaryTree()
        self.assertIsNone(myTree.root)

    def testInsert(self):
        myTree = BinaryTree()
        myTree.insert(2)
        self.assertEqual(myTree.root.getValue(), 2)
        self.assertEqual(str(myTree), '(2, 1, None, None)')

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

    def testIsBST(self):
        myTree = BinaryTree()
        self.assertTrue(myTree.isBST())
        myTree.insert(10)
        self.assertTrue(myTree.isBST())

    def testPrintPostorder(self):
        captured_output = io.StringIO()
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        with contextlib.redirect_stdout(captured_output):
            myTree.printPostorder()
        self.assertEqual(captured_output.getvalue(), "1 1\n3 1\n2 1\n")

    def testPrintInorder(self):
        captured_output = io.StringIO()
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        with contextlib.redirect_stdout(captured_output):
            myTree.printInorder()
        self.assertEqual(captured_output.getvalue(), "1 1\n2 1\n3 1\n")

    def testPrintPreorder(self):
        captured_output = io.StringIO()
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        with contextlib.redirect_stdout(captured_output):
            myTree.printPreorder()
        self.assertEqual(captured_output.getvalue(), "2 1\n1 1\n3 1\n")

    def testRepr(self):
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        self.assertEqual(str(myTree), "(2, 1, (1, 1, None, None), (3, 1, None, None))")

    def testFind(self):
        myTree = BinaryTree()
        self.assertIsNone(myTree.find(2))
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        myTree.insert(3)
        self.assertEqual(myTree.find(2), 1)
        self.assertEqual(myTree.find(1), 1)
        self.assertEqual(myTree.find(3), 2)

    def testInvert(self):
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        self.assertEqual(str(myTree), "(2, 1, (1, 1, None, None), (3, 1, None, None))")
        myTree.invert()
        self.assertEqual(str(myTree), "(2, 1, (3, 1, None, None), (1, 1, None, None))")

    def testTotal(self):
        myTree = BinaryTree()
        self.assertEqual(myTree.total(), 0)
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        myTree.insert(3)
        self.assertEqual(myTree.total(), 4)

    def testRandomInsert(self):
        myTree = BinaryTree()
        count_insertions = 1000
        for _ in range(count_insertions):
            value = randint(0,20)
            myTree.insert(value)
        self.assertEqual(myTree.total(), count_insertions)

    def testSize(self):
        myTree = BinaryTree()
        self.assertEqual(myTree.size(), 0)
        values = [10,7,8,13,17,5,6,11,12,3,4,15,16,14,1,2,18,20,0,19,9]
        for i in values:
            myTree.insert(i)
        self.assertEqual(myTree.size(), len(values))

    def testDeleteRoot(self):
        myTree = BinaryTree()
        self.assertIsNone(myTree.root)
        myTree.insert(8)
        self.assertIsNotNone(myTree.root)
        myTree.delete(8)
        self.assertIsNone(myTree.root)

    def testDelete(self):
        myTree = BinaryTree()
        values = [10,7,8,13,17,5,6,11,12,3,4,15,16,14,1,2,18,20,0,19,9]
        for i in values:
            myTree.insert(i)
        myTree.delete(8)
        self.assertIsNone(myTree.find(8))
        self.assertEqual(myTree.size(), len(values) - 1)
