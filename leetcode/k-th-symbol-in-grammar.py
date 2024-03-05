class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def gra(n,k):
            if n == 1:
                return 0
            
            mid = 2**(n-1) //2
            if k<=mid:
                return gra(n-1,k)
            else:
                return (gra(n-1,k-mid)+ 1) %2
        return gra(n,k)
        

            
        