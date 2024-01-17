class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        flag = False
        N = len(nums)
        total = sum(nums)

        for i in range(N):
            right_sum = total - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum+=nums[i]
        return -1
            

        