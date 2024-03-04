class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        bucket = []
        ans = []
        candidates.sort()
        def backtrack(idx):
            if sum(bucket) == target: 
                ans.append(bucket.copy())
                return
            if sum(bucket) > target:
                return
            i = idx
            while i < len(candidates):

                bucket.append(candidates[i])
                backtrack(i+1)
                bucket.pop()
                i+=1
                while i > 0 and i < len(candidates) and candidates[i] == candidates[i-1]:
                    i+=1

        backtrack(0)        
        return ans
        