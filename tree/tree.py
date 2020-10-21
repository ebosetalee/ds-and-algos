from treenode.treenode import TreeNode


class Tree:
    def __init__(self):
        """
        Initialize the Binary Tree here
        """
        self.root = None

    def add_child(self, value, current_node=None):
        """"
        Adds descendant to the tree

        :param value: child to be added
        :param current_node: To indicate the parent
        :returns: True if child is added, False if child in existence
        """
        if not self.root:
            self.root = TreeNode(value)
            return True
        else:
            if not current_node:
                if self.add_child(value, self.root):
                    return True
                else:
                    return False
            else:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = TreeNode(value)
                        current_node.left.parent = current_node
                        return True
                    else:
                        self.add_child(value, current_node.left)
                elif value > current_node.value:
                    if not current_node.right:
                        current_node.right = TreeNode(value)
                        current_node.right.parent = current_node
                        return True
                    else:
                        self.add_child(value, current_node.right)
                else:
                    return False

    def display(self):
        """
        Prints out all the items in the tree starting from the root

        :returns: An array of the items in the tree
        """
        if self.root:
            return self._display(self.root)

    def _display(self, current_node=None):
        """
        Prints out all the items in the tree starting from the root

        :param current_node: Indicates the parent
        :returns: An array of the items in the tree from left
        """
        elements = [current_node.value]
        if current_node.left:
            elements += self._display(current_node.left)
        if current_node.right:
            elements += self._display(current_node.right)
        return elements

    def find(self, value):
        """
        Searches the tree for the value

        :param value: value searched for
        :returns: True if found, False is not in the tree
        """
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return True
            elif value < current_node.value and current_node.left:
                current_node = current_node.left
                continue
            elif value > current_node.value and current_node.right:
                current_node = current_node.right
                continue
            else:
                return False

    def search(self, value):
        """
        Searches the tree for the value in the tree

        :param value: value searched for
        :returns: node if found, False if not in the tree
        """
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value and current_node.left:
                current_node = current_node.left
                continue
            elif value > current_node.value and current_node.right:
                current_node = current_node.right
                continue
            else:
                return False

    def get_parent(self, value):
        """
        Finds the parent of a child

        :param value: The child
        :returns: The parent value of the child
        """
        parent = self.search(value).parent
        return parent.value

    def delete(self, value):
        """
        Deletes the value from the tree and rearranges the tree

        :param value: Value to be deleted
        :return: True if deleted and False if not in the tree
        """
        if not self.search(value):
            return False
        else:
            node = self.search(value)

        def min_value(current_node):
            while current_node.left:
                current_node = current_node.left
            return current_node.value

        if not node.left and not node.right:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
            return True

        elif (node.left and not node.right) or (node.right and not node.left):
            if node.left:
                child = node.left
            else:
                child = node.right

            if node.parent:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child
            return True

        elif node.left and node.right:
            successor = min_value(node.right)
            self.delete(successor)
            node.value = successor
            return True
