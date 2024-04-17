# single Linked List

class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node

        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def deleteduplicates(self,head):

        if not head:
            return

        current=head
        while current.next:
            if current.value==current.next.value:
                current.next=current.next.next
            else:
                current=current.next


    def display(self):
        current=self.head
        while current:
            print(current.value,end="->")
            current=current.next
        print("None")


n1=Node(3)
n2=Node(4)
n3=Node(4)
n4=Node(6)
ll=LinkedList()
ll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
print("Linked List:")
ll.display()
ll.insert(7)
ll.display()
ll.deleteduplicates(n1)
ll.display()

