class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        wd = list(palindrome)

        if n == 1:
            return ""
        
        mx = ['z']*(n+1)
        for i in range(n):
            temp = wd[i]
            if wd[i] == 'a':
                wd[i] = 'b'
                if len(set(wd)) == 1:
                    wd[i] = temp
                    continue
                mx = min(mx,wd).copy()
                wd[i] = temp
            else:
                wd[i] = 'a'
                if len(set(wd)) == 1:
                    wd[i] = temp
                    continue
                mx = min(mx,wd).copy()
                wd[i] = temp
        

        an = "".join(mx)
        return an