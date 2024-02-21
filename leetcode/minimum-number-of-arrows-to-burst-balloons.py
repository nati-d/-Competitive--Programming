class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        c = 1
        curr = 0
        ind = 1


        while ind<len(points):
            if points[curr][1] < points[ind][0]:
                curr = ind
                c+=1
                ind = curr+1
                continue
            ind+=1
        print(points)
        return c