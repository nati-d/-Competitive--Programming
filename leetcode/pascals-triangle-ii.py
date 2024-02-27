class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(n):
            if n==0:
                return [1]
            if n == 1:
                return [1,1]
            
            prev = helper(n-1)
            curr = []
            for i in range(len(prev) - 1):
                curr.append(prev[i] + prev[i+1])
            curr.insert(0,1)
            curr.append(1)
            return curr           

        return helper(rowIndex)