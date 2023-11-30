class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = len(strs[0])
        res=''
        for string in strs:
            if len(string) < min:
               min = len(string)
        
        for i in range(min):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0][:min]