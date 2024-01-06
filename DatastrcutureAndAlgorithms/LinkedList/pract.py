############# for my Purpose
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def list_is_empty(self):
        return not self.head

    def insert_at_begining(self, new_node):
        if self.list_is_empty():
            self.head=new_node
        else:
            new_node.next = self.head
            self.head=new_node
    
    def print(self):
        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.next
    
if __name__ == '__main__':
     root=LinkedList()
     root.insert_at_begining(Node(5))
     root.insert_at_begining(Node(4))
     root.insert_at_begining(Node(3))

     root.print()

    
################## Upgerade 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def list_is_empty(self):
        return not self.head

    def insert_at_begining(self, data):
        new_node = Node(data)  # Creating a Node object with the given data
        if self.list_is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
    
if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_begining(5)
    root.insert_at_begining(4)
    root.insert_at_begining(3)

    root.print()
