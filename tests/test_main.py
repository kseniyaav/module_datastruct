import unittest
from src.main import Stack


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


if __name__ == '__main__':
    unittest.main()