class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        k = len(p)
        ans = []
        l =0
        r = k-1

        tp = list(p)
        tp.sort()

        while l<= N-k:
            tm = s[l:r+1]
            tm = list(tm)
            tm.sort()
            if tm == tp:
                ans.append(l)
            l+=1
            r+=1
        return ans

        