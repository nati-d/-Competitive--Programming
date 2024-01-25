# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        cur = head

        while cur:
            lst.append(cur.val)
            cur = cur.next
        a = lst[::-1]
        print(lst,a)
        if lst == a:
            return True
        else:
            return False
        