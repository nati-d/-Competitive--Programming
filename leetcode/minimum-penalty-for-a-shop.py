class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ind = 0
        mn = inf
        customers = list(customers)

        for i in range(len(customers)):
            if customers[i] == 'Y':
                customers[i] = 1
            else:
                customers[i] = 0
        sm = sum(customers)
        mn = min(mn,sm)
        for i in range(len(customers)):
            if customers[i] == 1:
                sm-=1
            else:
                sm+=1
            if sm < mn:
                ind = i+1
            mn = min(mn,sm)
        return ind