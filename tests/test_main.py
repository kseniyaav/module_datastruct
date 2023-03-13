import unittest
from src.main import Stack, LinkedList


class TestStack(unittest.TestCase):

    def test_push_one_element(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top.data, 1)

    def test_push_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top.data, 3)
        self.assertEqual(stack.top.next_node.data, 2)
        self.assertEqual(stack.top.next_node.next_node.data, 1)

    def test_push_string(self):
        stack = Stack()
        stack.push("hello")
        self.assertEqual(stack.top.data, "hello")

    def test_push_list(self):
        stack = Stack()
        stack.push([1, 2, 3])
        self.assertEqual(stack.top.data, [1, 2, 3])

    def test_push_dict(self):
        stack = Stack()
        stack.push({"key": "value"})
        self.assertEqual(stack.top.data, {"key": "value"})

    def test_push_on_empty_stack(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top.data, 1)

    def test_pop_empty_stack(self):
        stack = Stack()
        popped = stack.pop()
        self.assertIsNone(popped)
        self.assertIsNone(stack.top)

    def test_pop_single_element_stack(self):
        stack = Stack()
        stack.push(1)
        popped = stack.pop()
        self.assertEqual(popped, 1)
        self.assertIsNone(stack.top)

    def test_pop_multiple_element_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        popped = stack.pop()
        self.assertEqual(popped, 3)
        self.assertEqual(stack.top.data, 2)

    def test_peek_empty_stack(self):
        stack = Stack()
        peeked = stack.peek()
        self.assertIsNone(peeked)
        self.assertIsNone(stack.top)

    def test_peek_single_element_stack(self):
        stack = Stack()
        stack.push(1)
        peeked = stack.peek()
        self.assertEqual(peeked, 1)
        self.assertEqual(stack.top.data, 1)

    def test_peek_multiple_element_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        peeked = stack.peek()
        self.assertEqual(peeked, 3)
        self.assertEqual(stack.top.data, 3)

    def test_peek_after_pop(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        peeked = stack.peek()
        self.assertIsNone(peeked)
        self.assertIsNone(stack.top)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.tail.data, {'id': 1})

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 3})

    def test_print_ll(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.print_ll(), ' {\'id\': 0} -> {\'id\': 1} -> {\'id\': 2} -> {\'id\': 3} -> None')


if __name__ == '__main__':
    unittest.main()
