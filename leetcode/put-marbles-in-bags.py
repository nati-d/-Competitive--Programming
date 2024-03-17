class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = []
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        print(arr)
        arr.sort()
        print(arr)
        mx = sum(arr[len(arr)-k+1:])
        mn = sum(arr[:k-1])
        return mx-mn