class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        r=0
        count = 0

        while r<=N-k:
            w = s[r:r+k]
            c = w.count('a') + w.count('e') + w.count('i') + w.count('o') + w.count('u')
            count = max(count, c)
            r+=1
        return count
        