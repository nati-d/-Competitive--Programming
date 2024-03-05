class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n1 = [1,2,3]
        n2 = [4,5,6]
        ans = []
        bucket = []


        def backtrack(left,right):
            if len(bucket) >= 2*n:
                ans.append("".join(bucket.copy()))
                return
            if left < n:
                bucket.append('(')
                backtrack(left+1,right)
                bucket.pop()
            if right < left:
                bucket.append(')')
                backtrack(left,right+1)
                bucket.pop()
        backtrack(0,0)
        return ans

            
