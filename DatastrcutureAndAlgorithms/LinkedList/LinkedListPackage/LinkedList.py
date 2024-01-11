 
class Node:
    def __init__(self,data):
        self.data = data
        self.next =None


class LinkedList:
    def __init__(self):
        self.head= None
    
    def list_is_empty(self):
        return not self.head
    
    def insert_at_begining(self,data):
        newNode = Node(data)
        if self.list_is_empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_at_ending(self,data):
        newNode = Node(data)
        if self.list_is_empty():
            self.head = newNode
        else:
            itr = self.head
            while itr.next != None:
                itr=itr.next
            itr.next =newNode
    
    def getLength(self):
        if self.list_is_empty():
            return "Linked List is Empty ):"
        else:
            itr = self.head
            counter = 0
            while(itr):
                counter+=1
                itr=itr.next
                
            return counter 

    def insert_at_index(self,index,data):
        newNode = Node(data)
        if self.list_is_empty():  
             print("Linked List is Empty :(")
        elif  index>self.getLength():  
            print('index is out of range..:{') 
        elif index == index>self.getLength()-1:
            self.insert_at_ending(data)

        else:
            i=0 
            itr = self.head
            NextNode = None
            while(i<index-1):
                itr = itr.next
                i+=1
            NextNode = itr.next
            newNode.next = NextNode
            itr.next = newNode

    def del_at_beginning(self):
        if not self.list_is_empty():   
            temp = self.head
            self.head = temp.next
            del temp

    def del_at_ending(self):
        if not self.list_is_empty():  # Highlight: Added check for an empty list
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            del temp.next
            temp.next = None
    
    def get_middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow = slow.next
        return slow.data

 

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


root = LinkedList()
root.insert_at_begining(1)
root.insert_at_begining(2)
root.insert_at_begining(3)
root.insert_at_begining(4)
root.insert_at_begining(5)
# root.display()
print(root.get_middle())

 
