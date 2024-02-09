class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


list1 = [1, 2, 4]
list2 = [1, 3, 4]
linked_list1 = list_to_linkedlist(list1)
linked_list2 = list_to_linkedlist(list2)
merged_list = merge_two_lists(linked_list1, linked_list2)
print(linkedlist_to_list(merged_list)) 

list3 = []
list4 = []
linked_list3 = list_to_linkedlist(list3)
linked_list4 = list_to_linkedlist(list4)
merged_list_empty = merge_two_lists(linked_list3, linked_list4)
print(linkedlist_to_list(merged_list_empty)) 

list5 = []
list6 = [0]
linked_list5 = list_to_linkedlist(list5)
linked_list6 = list_to_linkedlist(list6)
merged_list_single = merge_two_lists(linked_list5, linked_list6)
print(linkedlist_to_list(merged_list_single)) 

list7 = []
list8 = [1, 2, 3, 4, 5]
linked_list7 = list_to_linkedlist(list7)
linked_list8 = list_to_linkedlist(list8)
merged_list_long_empty = merge_two_lists(linked_list7, linked_list8)
print(linkedlist_to_list(merged_list_long_empty)) 

list9 = [0, 1, 9]
list10 = [3, 4, 5]
linked_list9 = list_to_linkedlist(list9)
linked_list10 = list_to_linkedlist(list10)
merged_list_mixed = merge_two_lists(linked_list9, linked_list10)
print(linkedlist_to_list(merged_list_mixed))
