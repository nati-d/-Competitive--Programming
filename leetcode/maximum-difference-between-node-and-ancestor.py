# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def maxA(nd,maxx,minn):
            nonlocal ans
            if not nd:
                ans = max(ans, maxx-minn)
                return []
            
            maxx = max(maxx, nd.val)
            minn = min(minn,nd.val)

            ls = maxA(nd.left,maxx,minn)
            rs = maxA(nd.right,maxx,minn)

            return ls and rs
            
            
        maxA(root,0,100000000)
        return ans

        