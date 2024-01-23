class Solution:
    def maxScore(self, s: str) -> int:
        s = list(map(int,s))
        zero = 0
        one = sum(s[1:])

        if s[0] == 0:
            zero+=1
        mx = zero+one

        for i in range(1,len(s)-1):
            if s[i] == 0:
                zero+=1
            else:
                one-=1
            mx = max(mx,zero+one)
        return mx