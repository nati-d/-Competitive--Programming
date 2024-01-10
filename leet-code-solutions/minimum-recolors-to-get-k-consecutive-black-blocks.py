class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 1000

        r = 0
        N = len(blocks)

        while r<=N-k:
            count = min(blocks[r:r+k].count('W'),count)
            r+=1
        return count

        