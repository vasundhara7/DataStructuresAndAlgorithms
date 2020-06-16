class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def append(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
a=LinkedList()
a.push(9)
a.push(10)
a.push(12)
a.push(14)
a.append(20)
a.append(21)
a.printList()

