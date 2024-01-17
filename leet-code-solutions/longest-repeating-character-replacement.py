class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        N =  len(s)
        counter = defaultdict(int)
        mx = 0

        for right in range(N):
            counter[s[right]]+=1

            while right-left+1 - max(counter.values()) > k:
                counter[s[left]] -=1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left+=1
            mx = max(mx,right-left+1)
        return mx
