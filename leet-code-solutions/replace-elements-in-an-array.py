
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums)}
        arr = copy.deepcopy(nums)

        for opr in operations:
            if opr[0] in index_map:
                ind = index_map[opr[0]]
                arr[ind] = opr[1]
                index_map[opr[1]] = ind
                del index_map[opr[0]]  

        return arr
