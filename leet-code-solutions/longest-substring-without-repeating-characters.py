class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        N = len(s)
        mx = 0
        temp = set()

        while r < N:
            temp.add(s[r])
            r += 1

            mx = max(mx, len(temp))

            while r< N-1 and l < r and s[r] in temp:
                temp.remove(s[l])
                l += 1

        return mx
