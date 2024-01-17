class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dct = defaultdict(int)
        N = len(fruits)

        l = 0
        mx = 0

        for r in range(N):
            dct[fruits[r]]+=1

            while len(dct) > 2 and l<=r:
                print(l)
                dct[fruits[l]]-=1
                if dct[fruits[l]] == 0:
                    del dct[fruits[l]]
                l+=1
            mx = max(mx,r-l+1)
        return mx

        
        