class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        smm = nums[0]

        for i in range(1,n):
            smm = max(nums[i], smm+nums[i])

            ans = max(smm,ans)

        return ans
        
        