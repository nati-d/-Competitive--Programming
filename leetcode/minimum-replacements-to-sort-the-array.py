class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        count = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > prev:
                count += ceil((nums[i]/prev)-1)
                prev = nums[i]//ceil(nums[i]/prev)
            else:
                prev = nums[i]
        print(count)
        return count