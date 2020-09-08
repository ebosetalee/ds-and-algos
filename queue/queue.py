from linked_list.linked_list import LinkedList


class Queue:
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
        return self.items.head is None

    def enqueue(self, value):
        """
        Adds the value to the back of the LinkedList
        :param value: the value to be added
        """
        self.items.add(value)

    def dequeue(self):
        """
        Removes the value at the head
        :return: the value of the item at the head
        """
        current_node = self.items.head
        if not self.items.head:
            return None
        self.items.head = self.items.head.next
        return current_node.value

    def peek(self):
        """
        :returns: the value of the item at the head
        """
        return self.items.head.value
