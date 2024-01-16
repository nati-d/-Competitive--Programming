class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0,nums[0]]
        self.N = len(nums)
        self.nums = nums
        for i in range(1,self.N):
            self.arr.append(self.arr[i] + self.nums[i])
        print(self.arr)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - (self.arr[left])

        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)