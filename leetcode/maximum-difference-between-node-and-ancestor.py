# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def maxA(nd):
            nonlocal mx
            # nonlocal mn
            if not nd.left and not nd.right:
                return [nd.val,nd.val]
            # mx = max(mx,nd.val)
            # mn = min(mn,nd.val)
            mn = nd.val
            mxn = nd.val
            if nd.left:
                a, b = maxA(nd.left)
                mx = max(mx,abs(nd.val-a), abs(nd.val-b))
                mn = min(mn,a)
                mxn = max(mxn,b)
            if nd.right:
                a, b = maxA(nd.right)
                mx = max(mx,abs(nd.val-a), abs(nd.val-b))
                mn = min(mn,a)
                mxn = max(mxn,b)
            print(mn,mxn)
            return [mn,mxn]
            
        maxA(root)
        return mx

        