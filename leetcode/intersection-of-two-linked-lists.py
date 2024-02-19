class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic=set()
        curr=headA
        
        while curr:
            dic.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in dic:
                return curr
            curr=curr.next

        return None