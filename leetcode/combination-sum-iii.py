class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        bucket = []
        ans = []
        def backtrack(idx):
            if sum(bucket) == n and len(bucket) == k:
                bucket.sort() 
                if bucket not in ans:
                    ans.append(bucket.copy())
                return
            if sum(bucket) > n:
                return
            for i in range(idx,10):
                if i in bucket:
                    continue
                bucket.append(i)
                backtrack(i+1)
                bucket.pop()
        backtrack(1)        
        return ans