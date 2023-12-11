class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(arr)):
            ind = arr[i]
            dic[ind] +=1
        return (max(dic, key = lambda k: dic[k]))
