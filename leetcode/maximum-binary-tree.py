# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(arr,lb,ub):
            if lb > ub:
                return None
            mx = max(arr[lb:ub+1])
            ind = arr.index(mx)
            ls = tree(arr,lb,ind-1)
            rs = tree(arr,ind+1,ub)
            return TreeNode(mx,ls,rs)
        return tree(nums,0,len(nums)-1)
        


        