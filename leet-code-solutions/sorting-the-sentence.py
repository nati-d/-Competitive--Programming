class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        ans = ['']*len(lst)

        for i in range(len(lst)):
            key = int(lst[i][-1]) - 1
            ans[key] = lst[i][:-1]
        return ' '.join(map(str,ans))
        