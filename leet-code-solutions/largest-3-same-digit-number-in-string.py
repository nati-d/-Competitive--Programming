class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        
        if len(num)<3:
            return ""
        for i in range(len(num)-2):
            st =""
            if num[i] == num[i+1] == num[i+2]:
                st=num[i]+num[i+1]+num[i+2]
                if st>ans:
                    ans=st
        return ans
        