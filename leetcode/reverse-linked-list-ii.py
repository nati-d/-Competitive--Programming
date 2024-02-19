class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        i = 1
        curr = head
        lst = []
        while curr:
            if i >= left and i<=right:
                lst.append(curr.val)
            i+=1
            curr = curr.next
        lst.reverse()
        i = 1
        curr = head
        c= 0
        while curr:
            if i >= left and i<=right:
                curr.val = lst[c]
                c+=1
            i+=1
            curr = curr.next
        
        return head