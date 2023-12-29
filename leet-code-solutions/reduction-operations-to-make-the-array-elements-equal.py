class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        c = Counter(nums)
        lst = []
        count = 0
        for key,values in c.items() :
            lst.append(key)
        
        for i in range(len(lst)):
            count += (c[lst[i]]) * ((len(lst)-1) - i)
        
        return count


        