# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []

        def kt(nd):
            if not nd:
                return []
            
            kt(nd.left)
            lst.append(nd.val)
            kt(nd.right)
        kt(root)
        lst.sort()
        return lst[k-1]
        