import unittest
from queue.queue import Queue


class TestQueue(unittest.TestCase):
    def test_empty_list(self):
        queue = Queue()
        # assert that an empty linked list is created
        self.assertEqual(queue.items.head, None)
        self.assertEqual(queue.items.tail, None)
        self.assertEqual(queue.items.walk(), [])

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(13)
        queue.enqueue(31)
        self.assertEqual(queue.items.walk(), [1, 2, 13, 31])

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(13)
        queue.enqueue(31)
        # assert that the item dequeued was the item at the head
        self.assertEqual(queue.dequeue(), 1)
        # assert that the item at the head of the linked list was removed
        self.assertEqual(queue.items.walk(), [2, 13, 31])

    def test_peak(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.peek(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)
        queue.enqueue(13)
        self.assertEqual(queue.peek(), 1)
        queue.dequeue()
        self.assertEqual(queue.peek(), 2)


if __name__ == '__main__':
    unittest.main()
