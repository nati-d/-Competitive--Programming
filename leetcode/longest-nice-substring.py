class Solution:
    def longestNiceSubstring(self,s: str) -> str:
        def nice(cur):
            for char in set(cur):
                if char.upper() not in cur or char.lower() not in cur:
                    return False
            return True

        maxAnswer = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                current = s[i:j]
                if nice(current) and len(current) > len(maxAnswer):
                    maxAnswer = current

        return maxAnswer
