class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dct = Counter(t)
        n = len(dct)
        left = 0
        chr = 0
        mn = float('inf')
        minn = ""
        
        for right, char in enumerate(s):
            if char in dct:
                dct[char] -= 1
                if dct[char] == 0:
                    chr += 1
            
            while chr == n:
                if right - left + 1 < mn:
                    mn = right - left + 1
                    minn = s[left:right + 1]
                    
                if s[left] in dct:
                    dct[s[left]] += 1
                    if dct[s[left]] > 0:
                        chr -= 1
                left += 1
        
        return minn



        
        

        