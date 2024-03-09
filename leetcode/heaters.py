from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        arr = []

        for i in range(len(houses)):
            lft = bisect_left(heaters, houses[i])
            
            if lft == 0:
                arr.append(abs(heaters[lft] - houses[i]))
            elif lft == len(heaters):
                arr.append(abs(heaters[lft - 1] - houses[i]))
            else:
                arr.append(min(abs(heaters[lft] - houses[i]), abs(heaters[lft - 1] - houses[i])))
        
        return max(arr)
