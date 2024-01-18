class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = {0:1}
        count = 0
        p_arr= [0]

        for i in range(len(nums)):
            p_arr.append(p_arr[i]+nums[i])
        
        print(p_arr)

        for right in range(1,len(p_arr)):
            nm = p_arr[right] % k
            if nm in counter:
                count+=counter[nm]
                counter[nm] +=1
            else:
                counter[nm] = 1
        return count



        