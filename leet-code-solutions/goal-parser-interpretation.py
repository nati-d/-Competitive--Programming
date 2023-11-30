class Solution:
    def interpret(self, command: str) -> str:
        res=""
        a=command
        for i in range(len(a)):
            if a[i]=='G':
                res+=a[i]
            elif a[i]==')' and a[i-1]=='(':
                res+='o'
            elif a[i]=='l' and a[i-1]=='a' and a[i-2]=='(' and a[i+1]==')':
                res+='al'
            else:
                continue
        return res
                