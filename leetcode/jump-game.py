class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind = 0
        for i in range(len(nums)):
            ind = max(ind,i+nums[i])
            if i == ind:
                break
        if ind >=len(nums) - 1:
            return True
        else:
            return False