#python3 -m unittest btree_test

import unittest
import contextlib
import io
from btree import BinaryTree

class TestTree(unittest.TestCase):

    def testCreate(self):
        myTree = BinaryTree()
        self.assertIsNone(myTree.root)

    def testInsert(self):
        myTree = BinaryTree()
        myTree.insert(2)
        self.assertEqual(myTree.root.getValue(), 2)
        self.assertEqual(str(myTree), '(2, 0, None, None)')

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

    def testPrintPostorder(self):
        captured_output = io.StringIO()
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        with contextlib.redirect_stdout(captured_output):
            myTree.printPostorder()
        self.assertEqual(captured_output.getvalue(), "1 0\n3 0\n2 0\n")

    def testPrintInorder(self):
        captured_output = io.StringIO()
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        with contextlib.redirect_stdout(captured_output):
            myTree.printInorder()
        self.assertEqual(captured_output.getvalue(), "1 0\n2 0\n3 0\n")

    def testPrintPreorder(self):
        captured_output = io.StringIO()
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        with contextlib.redirect_stdout(captured_output):
            myTree.printPreorder()
        self.assertEqual(captured_output.getvalue(), "2 0\n1 0\n3 0\n")

    def testRepr(self):
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        self.assertEqual(str(myTree), "(2, 0, (1, 0, None, None), (3, 0, None, None))")

    def testFind(self):
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        myTree.insert(3)
        self.assertEqual(myTree.find(2), 0)
        self.assertEqual(myTree.find(1), 0)
        self.assertEqual(myTree.find(3), 1)

    def testInvert(self):
        myTree = BinaryTree()
        myTree.insert(2)
        myTree.insert(3)
        myTree.insert(1)
        self.assertEqual(str(myTree), "(2, 0, (1, 0, None, None), (3, 0, None, None))")
        myTree.invert()
        self.assertEqual(str(myTree), "(2, 0, (3, 0, None, None), (1, 0, None, None))")
