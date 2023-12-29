class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst = list(map(str,nums))



        for i in range(len(lst)-1):
            for j in range(i+1,len(lst)):
                if lst[i] + lst[j] > lst[j] + lst[i]:
                    continue
                else:
                    lst[i],lst[j] = lst[j], lst[i]
        if lst.count('0') == len(lst):
            return '0'
        return ''.join(lst)


        

                

            
        

        
        