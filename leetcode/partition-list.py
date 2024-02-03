# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        Lx = ListNode(0)
        Gx = ListNode(0)

        Lxp = Lx
        Gxp = Gx

        while head:
            if head.val < x:
                Lxp.next = head
                Lxp = Lxp.next
            else:
                Gxp.next = head
                Gxp = Gxp.next

            head = head.next

        Lxp.next = Gx.next

        Gxp.next = None

        return Lx.next
                