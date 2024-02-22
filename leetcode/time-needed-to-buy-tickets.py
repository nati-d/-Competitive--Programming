class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k]:
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                time+=1
                if tickets[k] == 0:
                    break
        return time
            

        