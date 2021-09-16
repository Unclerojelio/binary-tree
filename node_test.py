import unittest
import contextlib
import io
import sys
from node import Node

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1


class TestNode(unittest.TestCase):

    def testInit(self):
        n = Node()
        self.assertIsNone(n.getValue())
        self.assertEqual(n.getCount(), 0)
        self.assertIsNone(n.parent)
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

    def testGetParent(self):
        n = Node()
        self.assertIsNone(n.getParent())

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

    def testInsert(self):
        root = Node(2)
        root.insert(1)
        root.insert(3)
        self.assertEqual(str(root), "(2, 1, (1, 1, None, None), (3, 1, None, None))")

    def testDelete(self):
        root = Node(2)
        root.insert(1)
        root.insert(3)
        root.delete(3)
        self.assertEqual(str(root), "(2, 1, (1, 1, None, None), None)")
        root.delete(1)
        self.assertEqual(str(root), "(2, 1, None, None)")
        root.delete(2)
        #self.assertEqual(str(root), "(0, 0, None, None)")

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

    def testIsBST(self):
        a = Node(20)
        b = Node(10)
        c = Node(30)
        d = Node(5)
        e = Node(40)
        a.left = b
        a.right = c
        c.left = d
        c.right = e
        self.assertFalse(a.isBST(INT_MIN, INT_MAX))
        d.value = 21
        self.assertTrue(a.isBST(INT_MIN, INT_MAX))

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
        self.assertEqual(str(n), "(3, 2, None, None)")

    def testFind(self):
        n = Node(3)
        n.incrementCount()
        self.assertEqual(n.find(3), 2)

    def testTotal(self):
        n = Node()
        n.incrementCount()
        m = Node()
        m.incrementCount()
        o = Node()
        o.incrementCount()
        n.addLeftChild(m)
        n.addRightChild(o)
        self.assertEqual(n.total(), 3)

    def testFindMin(self):
        root = Node()
        values = [10,7,8,13,17,5,6,11,12,3,4,15,16,14,1,2,18,20,0,19,9]
        for value in values:
            root.insert(value)
        self.assertEqual(root.find_min().getValue(), 0)

    def testCountChildren(self):
        n = Node()
        m = Node()
        o = Node()
        self.assertEqual(n.count_children(), 0)
        n.addLeftChild(m)
        n.addRightChild(o)
        self.assertEqual(n.count_children(), 2)
