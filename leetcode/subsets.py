class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []


        def backtrack(idx):
            if idx >= len(nums):
                ans.append(bucket.copy())
                return
            
            bucket.append(nums[idx])
            backtrack(idx+1)
            bucket.pop()
            backtrack(idx+1)
        backtrack(0)
        return ans

        