# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        visited = set()
        ans = []
        def low(nd,target):
            if not nd:
                return
            
            if nd.val in visited:
                ans.append(nd)
            visited.add(nd.val)
            if nd.val == target:
                return nd
            if nd.val > target:
                return low(nd.left,target)
            else:
                return low(nd.right,target)
        low(root,p.val)
        low(root,q.val)

        return ans[-1]


            
            
        