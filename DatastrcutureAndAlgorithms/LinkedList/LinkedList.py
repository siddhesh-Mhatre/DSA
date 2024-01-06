class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count

    def print(self):
        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.next

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next= Node(data)

    def insert_at_index(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        itr = self.head
        count=0
        while itr.next:
             if count == index-1:
                node= Node(data,itr.next)
                itr.next = node 
                break
             itr = itr.next
             count +=1


    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index") 
        if index==0:
            self.head=self.head.next
            return
        itr= self.head
        count=0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr =itr.next
            count +=1

            
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)         
if __name__ == '__main__':
     root=LinkedList()
    #  root.insert_at_begining(11)
    #  root.insert_at_begining(22)
    #  root.insert_at_begining(33)
    #  root.insert_at_begining(44)
    #  root.insert_at_begining(55)


     root.insert_values([1,2,3,4,5])
     root.remove_at(0)
    #  root.insert_at_index(1,22)
     root.print()
