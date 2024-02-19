# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummy = dummyNode

        curr = head
        while curr:
            temp = curr.next
            dummy= dummyNode
            while dummy.next and dummy.next.val < curr.val:
                dummy = dummy.next
            if dummy.next == None:
                dummy.next = curr
                curr.next = None
            else:
                nxt = dummy.next
                dummy.next = curr
                curr.next=nxt
            curr = temp
        return dummyNode.next


        