class LinkedListNode:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        pass

    def remove(self, value):
        pass

    def contains(self, value):
        return False

    def __str__(self):
        # No need to mess with this function -
        # Really important to understand.
        node_strings = list()

        # Go through all the nodes and gather the string representations.
        current = self.head
        while current is not None:
            node_strings.append(str(current))
            current = current.pointer

        return "->".join(node_strings)


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = LinkedListNode(1)
    ll.head.pointer = LinkedListNode(2)
    ll.head.pointer.pointer = LinkedListNode(3)

    print(ll)
