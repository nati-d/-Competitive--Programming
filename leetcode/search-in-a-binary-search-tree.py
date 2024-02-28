# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def tr(nd,val):
            if not nd:
                return None
            if nd.val == val:
                return nd
            elif nd.val < val:
                return tr(nd.right,val)
            else:
                return tr(nd.left,val)
        return tr(root,val)
            



        