import unittest
from src.main import Node
from src.custom_queue import Queue, Node

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

    def test_dequeue_with_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())

    def test_dequeue_with_one_element(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.dequeue(), 'data1')

    def test_dequeue_with_multiple_elements(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')

    def test_dequeue_with_head_and_tail_pointing_to_same_node(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_dequeue_with_multiple_elements_until_empty(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertIsNone(queue.dequeue())
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

if __name__ == '__main__':
    unittest.main()

