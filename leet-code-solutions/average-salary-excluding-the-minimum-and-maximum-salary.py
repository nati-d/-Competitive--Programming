class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        s =0
        count =0
        for i in range(1,len(salary)-1):
            s+=salary[i]
            count+=1
        avr = s/count
        
        return avr
            
        