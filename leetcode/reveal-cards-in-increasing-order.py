class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        queue = deque()
        deck.sort(reverse = True)

        for i in range(len(deck)):
            if not queue:
                queue.append(deck[i])
            else:
                val =queue[-1]
                queue.pop()
                queue.appendleft(val)
                queue.appendleft(deck[i])
        return queue

