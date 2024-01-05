class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        l =0
        N = len(nums)
        r = N-1

        while l<r:
            if nums[l] + nums[r] > k:
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                c+=1
                r-=1
                l+=1
        return c        