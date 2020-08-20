from node.node import Node


class LinkedList:
    def __init__(self):
        """
        Initialize the LinkedList here
        """
        pass

    def get_head(self):
        pass

    def get_tail(self):
        pass

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

    def walk(self):
        """
        Prints out all the items in the list starting from the head

        :rtype: collections.Iterable[Node]
        :returns: An array of the items in the list
        """
        pass

    def search(self, value):
        """
        Searches the list to see if an item is inside

        :param value: The item searched for
        :returns: True if the value was found, or False if the value was not found 
        """
        pass
