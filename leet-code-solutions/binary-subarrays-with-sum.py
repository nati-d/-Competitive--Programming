class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = {0:1}
        count = 0
        p_arr= [0]

        for i in range(len(nums)):
            p_arr.append(p_arr[i]+nums[i])
        
        print(p_arr)

        for right in range(1,len(p_arr)):
            nm = p_arr[right] - goal
            if nm in counter:
                count+=counter[nm]
        
            if p_arr[right] in counter:
                counter[p_arr[right]] += 1
            else:
                counter[p_arr[right]] = 1
        return count



        