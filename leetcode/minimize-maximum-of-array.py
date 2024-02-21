class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0]*n
        sm = 0
        mx = 0
        for i in range(n):
            sm+= nums[i]
            mx =  max(mx,ceil(sm/(i+1)))
        
        return mx