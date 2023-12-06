class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res =[]
        for i in range(len(boxes)):
            sum = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                if boxes[j] == '1':
                    sum+= abs(i-j)
            res.append(sum)
        return res