class Solution:
    def largestOddNumber(self, num: str) -> str:
        mx = ""
        i = len(num)-1

        while i>=0:
            if int(num[i])%2 != 0:
                mx += num[0:i+1]
                break
            i-=1
        return mx
            
