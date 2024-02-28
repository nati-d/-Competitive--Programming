# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(ndl,ndr):
            if not ndl and not ndr:
                return True
            if not ndl or not ndr:
                return False
            
            if ndl.val != ndr.val:
                return False
            a = sym(ndl.left,ndr.right)
            b = sym(ndl.right,ndr.left)
            
            return a and b

            
        return sym(root.left,root.right)
        
        