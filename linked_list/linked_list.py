from node.node import Node


class LinkedList:
    def __init__(self):
        """
        Initialize the LinkedList here
        """
        self.head = None
        self.tail = self.head

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            current_node = self.tail
            current_node.next = new_node
            self.tail = current_node.next

    def prepend(self, value):
        """
        Adds the value to the start of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def remove(self, value):
        """
        Finds the vales and removes it

        :param value: the value to be removed
        :return: True if the value was removed, or False if the value isn't in the list
        """
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.value == value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False

    def walk(self):
        """
        Prints out all the items in the list starting from the head

        :rtype: collections.Iterable[Node]
        :returns: An array of the items in the list
        """
        elements = []
        current_node = self.head
        while current_node:
            # is the same as while current_node.next != None: or is not None
            elements.append(current_node.value)
            current_node = current_node.next
        return elements

    def search(self, value):
        """
        Searches the list to see if an item is inside

        :param value: The item searched for
        :returns: True if the value was found, or False if the value was not found 
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False
