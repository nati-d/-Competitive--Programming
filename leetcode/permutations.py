class Solution:    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []

        def backtrack(idx):
            if len(bucket) >= len(nums):
                ans.append(bucket.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in bucket:
                    continue
                bucket.append(nums[i])
                backtrack(i+1)
                bucket.pop()
        backtrack(0)
        return ans