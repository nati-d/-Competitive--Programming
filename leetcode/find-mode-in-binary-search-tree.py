# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = Counter()
        def inorder(nd):

            if nd:
                inorder(nd.left)
                c[nd.val] += 1
                inorder(nd.right)
        inorder(root)

        mx = max(c.values())

        lst = []
        for key,values in c.items():
            if values == mx:
                lst.append(key)
        return lst
