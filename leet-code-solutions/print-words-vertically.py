class Solution:
    def printVertically(self, s: str) -> List[str]:
        word = s.split()
        maxWord = len(word[0])
        ans=[]
        for i in range(len(word)):
            if len(word[i])>maxWord:
                maxWord = len(word[i])

        for i in range(len(word)):
            while len(word[i]) < maxWord:
                word[i]+=' '
        for i in range(maxWord):
            stri =""
            for j in range(len(word)):
               stri+=word[j][i]
            ans.append(stri.rstrip())
        return ans

