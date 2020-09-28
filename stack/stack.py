from linked_list.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def push(self, value):
        """
        Adds the value to the back of the LinkedList
        :param value: the value to be added
        """
        self.items.add(value)

    def pop(self):
        """
        Removes the value at the tail
        :return: the value of the item removed
        """
        if self.items.tail is None:
            return None
        value = self.items.tail.value
        self.items.remove(value)
        return value

    def peek(self):
        """
        :returns: the value of the item at the tail
        """
        return self.items.tail.value
