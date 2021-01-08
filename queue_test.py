import unittest
from queue import Queue

class TestQueue(unittest.TestCase):

    def testEnqueue(self):
        q = Queue()
        q.enqueue('A')
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.isEmpty())
        self.assertEqual(q.queue, ['A'])
        q.enqueue('B')
        self.assertEqual(q.queue, ['A', 'B'])

    def testDequeue(self):
        q = Queue()
        q.enqueue('A')
        q.enqueue('B')
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 'A')
        self.assertEqual(q.dequeue(), 'B')
        self.assertTrue(q.isEmpty())

    def testIsEmpty(self):
        q = Queue()
        q.enqueue('A')
        self.assertFalse(q.isEmpty())

    def testSize(self):
        q = Queue()
        q.enqueue('A')
        self.assertEqual(q.size(), 1)
