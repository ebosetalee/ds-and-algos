import unittest
from tree.tree import Tree


class MyTestCase(unittest.TestCase):
    def test_empty_tree(self):
        tree = Tree()
        self.assertIsNone(tree.root)
        self.assertIsNone(tree.display())

    def test_tree_root(self):
        tree = Tree()
        tree.add_child(5)
        self.assertEqual(tree.root.value, 5)

    def test_add_child(self):
        tree = Tree()
        tree.add_child(5)
        self.assertEqual(tree.add_child(2), True)

    def test_tree_add_children(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(2)
        tree.add_child(4)
        self.assertEqual(tree.display()[1:], [2, 4])

    def test_tree_add_child_already_in_tree(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(2)
        tree.add_child(4)
        self.assertEqual(tree.add_child(2), False)

    def test_display(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(2)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        tree.add_child(0)
        tree.add_child(8)
        tree.add_child(3)
        self.assertEqual(tree.display(), [5, 2, 1, 0, 4, 3, 7, 6, 9, 8])

    def test_find_in_tree(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        self.assertEqual(tree.find(4), True)
        self.assertEqual(tree.find(6), True)

    def test_find_not_in_tree(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        self.assertEqual(tree.find(8), False)
        self.assertEqual(tree.find(2), False)

    def test_get_parent(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        self.assertEqual(tree.get_parent(7), 5)


if __name__ == '__main__':
    unittest.main()
