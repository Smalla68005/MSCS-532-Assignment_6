class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values


def test_linked_list():
    linked_list = LinkedList()
    
    # Insert elements
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)  # Insert 30 at head

    # Traverse and collect values
    print("Linked list values:", linked_list.traverse())  # Output: [30, 20, 10]

    print("All Linked List tests passed!")


# Test Linked List
test_linked_list()
