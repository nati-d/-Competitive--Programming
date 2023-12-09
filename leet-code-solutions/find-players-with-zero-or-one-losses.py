class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeroLoss= []
        oneLoss = []
        matchesDic=defaultdict(int)

        for match in matches:
            matchesDic[match[0]]+=0

        for match in matches:
            matchesDic[match[1]]+=1
        print(matchesDic)

        for key, values in matchesDic.items():
            if values == 1:
                oneLoss.append(key)
            if values == 0:
                zeroLoss.append(key)
        zeroLoss.sort()
        oneLoss.sort()
        return [zeroLoss, oneLoss]
        
        
        