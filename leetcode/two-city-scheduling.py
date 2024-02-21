class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lsta = costs
        lstb = costs

        lsta.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)
        A = B = len(costs)/2
        total = 0

        for a , b in costs:
            if B == 0 or (A and a<=b):
                total+=a
                A-=1
            else:
                total +=b
                B-=1
        return total