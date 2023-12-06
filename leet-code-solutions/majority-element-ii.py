class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = math.floor(len(nums)/3)
        res = []
        for i in range(len(nums)):
            if nums.count(nums[i]) > n:
                if nums[i] in res:
                    continue
                else:
                    res.append(nums[i])
        return res
                