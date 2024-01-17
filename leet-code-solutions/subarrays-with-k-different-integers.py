class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def calc(value):
            counter = defaultdict(int)
            sm = 0
            N = len(nums)
            left = 0

            for right in range(N):
                counter[nums[right]] += 1

                while left < N and len(counter) > value:
                    counter[nums[left]] -=1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left+=1
                sm += right-left+1
            return sm

        
        return calc(k) - calc(k-1)

        

        
        