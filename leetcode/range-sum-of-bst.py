# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        lst = []
        sm = 0
        def ran(node):
            if not node:
                return
            
            ran(node.left)
            lst.append(node.val)
            ran(node.right)
        ran(root)

        for i in range(len(lst)):
            if lst[i] >= low and lst[i] <= high:
                sm+=lst[i]
        return sm
        