class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s.sort()
        g.sort()

        l = 0
        r=0

        while l<len(g) and r <len(s):
            if s[r] >= g[l]:
                count+=1
                l+=1
                r+=1
            elif g[l] > s[r]:
                r+=1
            else:
                l+=1
        return count
        