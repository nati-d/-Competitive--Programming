class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = 0
        closes= 0

        for i in range(len(s)):
            if s[i] == '(':
                opens += 1
            elif s[i]==')' and opens > 0:
                opens -= 1
            else:
                closes += 1

        
        
        return closes + opens if opens else closes
        