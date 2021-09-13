import unittest
import contextlib
import io
from node import Node

class TestNode(unittest.TestCase):

    def testInit(self):
        n = Node()
        self.assertIsNone(n.getValue())
        self.assertEqual(n.getCount(), 0)
        self.assertIsNone(n.getLeftChild())
        self.assertIsNone(n.getRightChild())
        n = Node(1)
        self.assertEqual(n.getValue(), 1)

    def testSetValue(self):
        n = Node()
        n.setValue(1)
        self.assertEqual(n.getValue(), 1)

    def testGetValue(self):
        n = Node(2)
        self.assertEqual(n.getValue(), 2)

    def testIncrementCount(self):
        n = Node()
        n.incrementCount()
        self.assertEqual(n.getCount(), 1)

    def testGetLeftChild(self):
        n = Node()
        self.assertIsNone(n.getLeftChild())

    def testGetRightChild(self):
        n = Node()
        self.assertIsNone(n.getRightChild())

    def testAddLeftChild(self):
        n = Node()
        m = Node()
        n.addLeftChild(m)
        self.assertIsNotNone(n.getLeftChild())

    def testAddRightChild(self):
        n = Node()
        m = Node()
        n.addRightChild(m)
        self.assertIsNotNone(n.getRightChild())

    def testHeight(self):
        n = Node()
        self.assertEqual(n.height(), 1)

    def testIsBalanced(self):
        n = Node()
        self.assertTrue(n.isBalanced())
        m = Node()
        n.addLeftChild(m)
        self.assertTrue(n.isBalanced())
        o = Node()
        m.addLeftChild(o)
        self.assertFalse(n.isBalanced())

    def testSwap(self):
        n = Node()
        m = Node()
        o = Node()
        n.addLeftChild(m)
        n.addRightChild(o)
        n.swap()
        self.assertEqual(n.getLeftChild(), o)
        self.assertEqual(n.getRightChild(), m)

    def testRepr(self):
        n = Node(3)
        n.incrementCount()
        self.assertEqual(str(n), "(3, 1, None, None)")

    def testFind(self):
        n = Node(3)
        n.incrementCount()
        self.assertEqual(n.find(3), 1)
