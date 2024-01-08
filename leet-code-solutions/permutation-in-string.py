class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        s2 = list(s2)
        k = len(s1)
        N = len(s2)
        r=0
        l=0

        while r<=N-k:
            wd = s2[r:r+k]
            wd.sort()
            if wd == s1:
                return True
            r+=1
        return False




        
        