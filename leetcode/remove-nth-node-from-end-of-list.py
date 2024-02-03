# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nm = 0
        cur = head

        while cur:
            nm+=1
            cur = cur.next
        c = nm-n

        cr = head
        i = 0

        if c == 0:
            return head.next
        while cr:
            if i == c - 1:
                if cr.next.next and cr.next:
                    cr.next = cr.next.next
                else:
                    cr.next = None
            i+=1
            cr = cr.next
        return head

        