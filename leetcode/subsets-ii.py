class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        nums.sort()
        def backtrack(idx):
            if bucket not in ans:
                ans.append(bucket.copy())
            for i in range(idx,len(nums)):
                bucket.append(nums[i])
                backtrack(i+1)
                bucket.pop()
        backtrack(0)
        ans.sort()
        return ans