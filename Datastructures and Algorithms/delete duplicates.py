class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

def deleteduplicates(head):
    if not head:
        return head
    current=head
    while current.next:
        if current.value==current.next.value:
            current.next=current.next.next
        else:
            current=current.next
    return head
def dispaly(head):
    current=head
    while current:
        print(current.value,end=" ")
        current=current.next
    print()


n1=ListNode(1)
n1.next=ListNode(1)
n1.next.next=ListNode(2)


deleteduplicates(n1)
dispaly(n1)

