# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def tr(nd1, nd2):
            if not nd1 and not nd2:
                return True
            if not nd1 or not nd2 or nd1.val != nd2.val:
                return False
            return tr(nd1.left, nd2.left) and tr(nd1.right, nd2.right)
        return tr(p,q)
            
            
                
        