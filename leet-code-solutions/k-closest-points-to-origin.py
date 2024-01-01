import math
class Solution:
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if math.sqrt((left[i][0] ** 2) + (left[i][1] ** 2)) <= math.sqrt((right[j][0] ** 2) + (right[j][1] ** 2)):
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr


    def kClosest(self, points, k):
        return self.mergeSort(points)[0:k]