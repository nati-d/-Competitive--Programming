# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ptrs = set()
        flag = False

        while cur:
            if cur in ptrs:
                return cur
                break
            ptrs.add(cur)
            cur = cur.next
        
        return None