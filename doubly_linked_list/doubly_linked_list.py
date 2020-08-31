from linked_list.linked_list import LinkedList
from node.node import Node


# This is a subclass of LinkedList
class DoublyLinkedList(LinkedList):
    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        pass

    def prepend(self, value):
        """
        Adds the value to the start of the list

        :param value: the value to be added
        """
        pass

    def remove(self, value):
        """
        Finds the vales and removes it

        :param value: the value to be removed
        :return: True if the value was removed, or False if the value isn't in the list
        """
        pass

    def walk_reverse(self):
        """
        Prints out all the items in the list starting from the tail to the head

        :rtype: collections.Iterable[Node]
        :returns: A reversed array of the items in the list
        """
        pass
