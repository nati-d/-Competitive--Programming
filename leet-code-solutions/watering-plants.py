class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        po = capacity
        for i in range(len(plants)):
            if plants[i]<=capacity:
                capacity-=plants[i]
                steps+=1
            else:
                steps+=i
                capacity = po 
                capacity-=plants[i]
                steps+=(i+1)
        return steps
                