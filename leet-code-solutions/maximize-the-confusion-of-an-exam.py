class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        l = 0
        r = 0
        ans = 0
        dct = {'T': 0, 'F': 0}

        while r < N:
            dct[answerKey[r]] += 1

            while (r - l + 1) - max(dct.values()) > k:
                dct[answerKey[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
