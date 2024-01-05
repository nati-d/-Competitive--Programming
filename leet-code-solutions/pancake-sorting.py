class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []

        for target in range(len(arr), 0, -1):
            index = arr.index(target)

            if index != target - 1:
                arr[:index + 1] = reversed(arr[:index + 1])
                arr[:target] = reversed(arr[:target])

                flips.extend([index + 1, target])

        return flips
        
        