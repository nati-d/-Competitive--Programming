class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        c = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones +=1
            else:
                c+=ones
        return c
        