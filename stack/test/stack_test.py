import unittest
from stack.stack import Stack


class TestStack(unittest.TestCase):
    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.items.head, None)
        self.assertEqual(stack.items.tail, None)
        self.assertEqual(stack.items.walk(), [])

    def test_push_to_empty_stack(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.items.head.value, 1)
        self.assertEqual(stack.items.walk(), [1])

    def test_push_to_non_empty_stack(self):
        stack = Stack()
        stack.push(2)
        self.assertIsNotNone(stack.items.head)
        stack.push(4)
        self.assertNotEqual(stack.items.head.value, 4)
        self.assertEqual(stack.items.tail.value, 4)

    def test_pop_from_empty_stack(self):
        pass

    def test_pop_from_non_empty_stack_(self):
        pass

    def test_peep_from_empty_stack(self):
        pass

    def test_peep_from_non_empty_stack_(self):
        pass


if __name__ == '__main__':
    unittest.main()