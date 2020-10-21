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

    def test_delete_root_node(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(4)
        tree.add_child(6)
        tree.delete(5)
        self.assertEqual(tree.display(), [6, 4])

    def test_delete_node_without_child(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        tree.add_child(8)
        self.assertEqual(tree.display(), [5, 1, 4, 7, 6, 9, 8])
        tree.delete(4)
        self.assertEqual(tree.display(), [5, 1, 7, 6, 9, 8])
        tree.delete(8)
        self.assertEqual(tree.display(), [5, 1, 7, 6, 9])

    def test_delete_node_with_one_child(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        tree.add_child(8)
        self.assertEqual(tree.display(), [5, 1, 4, 7, 6, 9, 8])
        tree.delete(9)
        self.assertEqual(tree.display(), [5, 1, 4, 7, 6, 8])
        tree.delete(1)
        self.assertEqual(tree.display(), [5, 4, 7, 6, 8])

    def test_delete_node_with_children(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(1)
        tree.add_child(4)
        tree.add_child(7)
        tree.add_child(9)
        tree.add_child(6)
        tree.add_child(8)
        self.assertEqual(tree.display(), [5, 1, 4, 7, 6, 9, 8])
        tree.delete(7)
        self.assertEqual(tree.display(), [5, 1, 4, 8, 6, 9])
        tree.delete(8)
        self.assertEqual(tree.display(), [5, 1, 4, 9, 6])

    def test_delete_not_in_the_tree(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(2)
        tree.add_child(7)
        self.assertEqual(tree.display(), [5, 2, 7])
        tree.delete(6)
        self.assertEqual(tree.display(), [5, 2, 7])


if __name__ == '__main__':
    unittest.main()
