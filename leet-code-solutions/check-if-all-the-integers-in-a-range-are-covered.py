class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        lst = []
        lst2=[]
        ranges.sort()
        for i in range(len(ranges)):
            for j in range(ranges[i][0], ranges[i][1]+1):
                lst.append(j)
        for i in range(left, right+1):
            lst2.append(i)
        print(lst)
        print(lst2)
        for i in range(len(lst2)):
            if lst2[i] not in lst:
                return False
        return True
        
