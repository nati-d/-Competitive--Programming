class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

   
        return [ j[1] for j in sorted([heights[i],names[i]]for i in range(len(names)))[::-1]]
        

        for i in range(len(names)):
            tenp=i
            for j in range(i+1,len(names)):
                if heights[j]>heights[tenp]:
                    tenp=j
            heights[i],heights[tenp]=heights[tenp],heights[i]
            names[i],names[tenp]=names[tenp],names[i]
        
        return names
        
        # for i in range(len(names) ):
        #     while heights[i] < heights[i-1] and i >= 0:
        #         names[i],names[i-1] =  names[i-1], names[i]
        #         heights[i],heights[i-1] =  heights[i-1], heights[i]
        #         i-=1
        # return names