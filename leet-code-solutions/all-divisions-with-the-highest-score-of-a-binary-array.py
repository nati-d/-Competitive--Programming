class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        rights = list(nums)
        res = defaultdict(list)

        count_zeros = 0
        count_ones = rights.count(1)
        
        for i in range(len(rights) + 1):
            res[count_zeros + count_ones].append(i)

            if i < len(rights):
                if rights[i] == 0:
                    count_zeros += 1
                else:
                    count_ones -= 1

        key = max(res)
        return res[key]



        
        