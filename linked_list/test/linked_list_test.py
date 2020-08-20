import unittest

from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_add_one_item(self):
        linked_list = LinkedList()
        linked_list.add(1)
        # assert that the item we inserted is at the head
        self.assertEqual(linked_list.head.value, 1)
        # assert that when only one item is in the list the head and the tail are the same
        self.assertEqual(linked_list.tail.value, 1)

    def test_add_two_items(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(22)
        self.assertEqual(linked_list.head.next.value, 22)
        self.assertEqual(linked_list.head.next.value, linked_list.tail.value)

    def test_prepend(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.prepend(20)
        self.assertEqual(linked_list.head.value, 20)
        self.assertEqual(linked_list.tail.value, 1)

    def test_remove_from_head(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.remove(2), True)
        self.assertEqual(linked_list.walk(), [4, 25, 20, 12])

    def test_remove_from_tail(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.remove(12), True)
        self.assertEqual(linked_list.walk(), [2, 4, 25, 20])

    def test_remove_from_middle(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.remove(25), True)
        self.assertEqual(linked_list.walk(), [2, 4, 20, 12])

    def test_remove_item_not_in_list(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.remove(0), False)
        self.assertEqual(linked_list.walk(), [2, 4, 25, 20, 12])

    def test_walk(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.walk(), [2, 4, 25, 20, 12])

    def test_walk_list_empty(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.walk(), [])

    def test_search_item_at_head(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.search(2), True)

    def test_search_item_at_tail(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.search(12), True)

    def test_search_item_at_middle(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(52)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.search(52), True)

    def test_search_item_not_in_list(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(52)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(linked_list.search(0), False)
