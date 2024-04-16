class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        current=self.head
        while current:
            print(current.value,end="->")
            current=current.next
        print("None")

n1=Node(3)
n2=Node(7)
n3=Node(2)
n4=Node(9)
ll=Linkedlist()
ll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
ll.display()
