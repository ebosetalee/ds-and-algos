from linked_list.linked_list import LinkedList


class Queue(LinkedList):
    """
    The queue uses a LinkedList internally to manage the items
    """

    def __init__(self):
        """
        Initialize the Queue with an empty LinkedList
        """
        self.items = LinkedList()

    def is_empty(self):
        """
        :returns: True if the LinkedList is empty and False if it isn't
        """
        if self.items.head is None:
            return True
        return False

    def enqueue(self, value):
        """
        Adds the value to the back of the LinkedList
        :param value: the value to be added
        """
        pass

    def dequeue(self):
        """
        Removes the value at the head
        :return: the value of the item at the head
        """
        pass

    def peek(self):
        """
        :returns: the value of the item at the head
        """
        pass
