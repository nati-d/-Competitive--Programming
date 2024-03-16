# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        c = 0
        l = k
        curr = head
        ans = []
        while curr:
            c+=1
            curr = curr.next
        print (c)
        nums = [c//k] * k
        c-=sum(nums) 
        i = 0
        while c>0 and i < k:
            nums[i]+=1
            c-=1
            i+=1
        psum= [0]
        sm = 0
        for j in range(len(nums)):
            sm +=nums[j]
            psum.append(sm)
        print(nums)
        print(psum)
        
        j = 0
        d = 0
        curr = head
        while curr:
            if d== psum[j]:
                ans.append(curr)
                j+=1
            d+=1
            curr = curr.next
        for nm in range(len(nums)):
            if nums[nm] == 0:
                ans.append(None)
        n = 0
        for a in ans:
            cntd = 0
            curr = a
            while curr:
                cntd+=1
                if cntd == nums[n]:
                    n+=1
                    curr.next = None
                    break
                curr = curr.next

            
        return ans

            
                
        

