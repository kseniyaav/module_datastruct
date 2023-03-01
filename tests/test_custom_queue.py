import unittest
from custom_queue import Queue, Node

class TestNode(unittest.TestCase):
    def test_init(self):
        data = "test data"
        next_node = Node("next data", None)
        node = Node(data, next_node)
        self.assertEqual(node.data, data)
        self.assertEqual(node.next_node, next_node)

class TestQueue(unittest.TestCase):
    def test_init(self):
        q = Queue()
        self.assertIsNone(q.head)
        self.assertIsNone(q.tail)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.head.data, 1)
        self.assertEqual(q.head.next_node.data, 2)
        self.assertEqual(q.tail.data, 3)
        self.assertIsNone(q.tail.next_node)

    def test_enqueue_empty_queue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.head.data, 1)
        self.assertEqual(q.tail.data, 1)
        self.assertIsNone(q.head.next_node)
        self.assertIsNone(q.tail.next_node)

    def test_enqueue_multiple(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.head.data, 1)
        self.assertEqual(q.head.next_node.data, 2)
        self.assertEqual(q.tail.data, 4)
        self.assertIsNone(q.tail.next_node)

if __name__ == '__main__':
    unittest.main()

