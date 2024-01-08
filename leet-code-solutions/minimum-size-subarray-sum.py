class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        l=0
        r=1
        lst=[]
        sm = nums[0]

        if N == 1 and sm>= target:
            return 1
        else:
            if sm>= target:
                lst.append(r-l)
            while r<N:
                
                sm += nums[r]

                while sm >= target:
                    lst.append(r-l+1)
                    sm-=nums[l]
                    l+=1
                r+=1
            if len(lst) == 0:
                return 0
            else:
                return min(lst)

        