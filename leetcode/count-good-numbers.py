class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = (10 ** 9) + 7
        def myPow (x,n):
            nonlocal mod
            if n == 2:
                return x* x
            
            if n== 1:
                return x
            if n == 0:
                return 1
            
            if n< 0:
                return 1/myPow(x % mod,abs(n))
            
            if n%2 == 0:
                return myPow((x*x) % mod, n//2)
            else:
                return myPow(x % mod, n-1) * (x % mod)
        odd = 0
        even = 0
        if n%2 == 0:
            odd = n//2
            even = n//2
        else:
            odd = n//2
            even = ceil(n/2)
        
        return (myPow(5,even) * myPow(4,odd)) % mod