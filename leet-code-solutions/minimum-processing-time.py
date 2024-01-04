class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        d = copy.deepcopy(tasks)
        d.sort()
        processorTime.sort()
        c = []
        for i in range(0,len(d),4):
            c.append(max(d[i:i+4]))
        c = c[::-1]
        n = len(processorTime)
        mx = 0

        for i in range(n):
            mx = max(mx, c[i] + processorTime[i])
        
        return mx
        

        