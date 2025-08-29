# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input:    the heads of two sorted linked lists
# Task:     merge the two linked lists together, in sorted order 
# Output:   the head of the merged linked list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode()
        if list1.val <= list2.val:
            current = list1
            list1 = list1.next
        else:
            current = list2
            list2 = list2.next
        dummy.next = current

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current, list1 = current.next, list1.next
            else:
                current.next = list2
                current, list2 = current.next, list2.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next