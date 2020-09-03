from linked_list.linked_list import LinkedList
from node.node import Node


# This is a subclass of LinkedList
class DoublyLinkedList(LinkedList):
    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.head.previous = None
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """
        Adds the value to the start of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        self.head.previous = new_node
        new_node.next = self.head
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
                if previous_node is None:
                    self.head = current_node.next
                    self.head.previous = None
                else:
                    if current_node == self.tail:
                        previous_node.next = None
                        self.tail = previous_node
                    else:
                        previous_node.next = current_node.next
                        current_node = current_node.next
                        current_node.previous = previous_node
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False

    def walk_reverse(self):
        """
        Prints out all the items in the list starting from the tail to the head

        :rtype: collections.Iterable[Node]
        :returns: A reversed array of the items in the list
        """
        elements = []
        current_node = self.head
        while current_node:
            # is the same as while current_node.next != None: or is not None
            elements.append(current_node.value)
            current_node = current_node.next
        return elements[::-1]
