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
        Searches the tree for the value
        :param value: value searched for
        :returns: node if found, False is not in the tree
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
