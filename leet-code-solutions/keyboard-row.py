class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 ="asdfghjkl"
        r3 = "zxcvbnm"
        ans = []
        temp = ""
        for i in range(len(words)):
            if words[i][0].lower() in r1:
                temp = r1
            elif words[i][0].lower() in r2:
                temp = r2
            elif words[i][0].lower() in r3:
                temp = r3
            st = ""
            for j in range(len(words[i])):
                if words[i][j].lower() in temp:
                    st+=words[i][j]
            if st == words[i]:
                ans.append(st)
        return ans

