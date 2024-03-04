class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        bucket = []
        ans = []

        def backtrack(idx):
            if sum(bucket) == target:
                ans.append(bucket.copy())
                return
            if sum(bucket) > target:
                return
            
            for i in range(idx,len(candidates)):
                bucket.append(candidates[i])
                backtrack(i)
                bucket.pop()
        backtrack(0)
        return ans
        