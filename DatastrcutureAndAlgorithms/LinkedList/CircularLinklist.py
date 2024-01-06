class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def list_is_empty(self):
        return self.tail is None

    def insert_value(self, data):
        new_node = Node(data)
        if self.list_is_empty():
            self.tail = new_node
            self.tail.next = self.tail  # Point to itself for circularity
        else:
            new_node.next = self.tail.next  # New node points to the head
            self.tail.next = new_node  # Tail points to the new node
            self.tail = new_node  # Update the tail to the new node

    def print_list(self):
        if not self.list_is_empty():
            itr = self.tail.next  # Start from the head
            while itr != self.tail:
                print(itr.data)
                itr = itr.next
            # Print the data of the tail node
            print(itr.data)

if __name__ == '__main__':
    root = CircularLinkedList()
    root.insert_value(5)
    root.insert_value(4)
    root.insert_value(3)

    root.print_list()
