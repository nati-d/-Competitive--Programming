# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        old = dummy
        lst1 = list1
        lst2 = list2

        while lst1 and lst2:
            if lst1.val <= lst2.val:
                old.next = lst1
                lst1 = lst1.next

            else:
                old.next = lst2
                lst2 = lst2.next
            old = old.next
        
        if lst1 != None:
            old.next = lst1
        else:
            old.next = lst2
                
        return dummy.next

        