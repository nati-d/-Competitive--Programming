class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n <2:
            return 2
        for i in range(1,n):
            res = n*i
            if res % 2 ==0 and res %n ==0:
                return res
                break