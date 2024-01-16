class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        mn= float('inf')

        for i, card in enumerate(cards):
            if card in dic:
                mn = min(mn, i - dic[card] + 1)
            dic[card] = i

        return mn if mn != float('inf') else -1
