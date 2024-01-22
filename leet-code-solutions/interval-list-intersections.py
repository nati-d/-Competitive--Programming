class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        s,e = 0,1
        i,j = 0,0
        
        while i < len(firstList) and j < len(secondList):
            a = firstList[i] 
            b = secondList[j] 
            if b[s] <= a[e] and b[e] >= a[s]:
                intersectionPoint = [max(a[s],b[s]),min(a[e],b[e])]
                res.append(intersectionPoint) 
                
            if a[e] > b[e]:
                j += 1
            else:
                i += 1
        return res