class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd = []
        even = 0
        for key,values in c.items():
            if values%2 == 0:
                even+=values
            else:
                odd.append(values)
        
        
        odd.sort(reverse = True)
        for i in range(1,len(odd)):
            even+= odd[i]-1
        

        return even + odd[0] if odd else even
        