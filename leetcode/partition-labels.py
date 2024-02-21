class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ss = set(s)
        dct = defaultdict(int)
        ans = []

        for char in ss:
            dct[char] = s.rindex(char)

        mx = 0
        mn = 0

        for i in range(len(s)):
            mx = max(mx,dct[s[i]])
            if i == mx:
                ans.append(mx-mn+1)
                mn = mx+1  
        return ans