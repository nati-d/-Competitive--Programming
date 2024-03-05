# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def sort(left,right):
            nonlocal n
            if left>right:
                return 

            mid = (left+right)//2

            left = sort(left,mid-1)
            right = sort(mid+1,right)
            return TreeNode(nums[mid],left,right)
        
        return sort(0,n-1)
        