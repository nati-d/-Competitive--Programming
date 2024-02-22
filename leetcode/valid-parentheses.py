class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(','[','{']
        closes = [")",']',"}"]

       
        for i in range(len(s)):
            if s[i] in opens:
                stack.append(s[i])
            elif s[i] in closes and len(stack) == 0:
                return False
            elif s[i] in closes  and opens.index(stack[-1]) != closes.index(s[i]) :
                return False
            elif s[i] in closes  and opens.index(stack[-1]) == closes.index(s[i]):
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
        