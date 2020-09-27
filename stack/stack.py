from linked_list.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def push(self, value):
        self.items.add(value)

    def pop(self):
        if self.items.tail is None:
            return None
        value = self.items.tail.value
        self.items.remove(value)
        return value

    def peek(self):
        return self.items.tail.value
