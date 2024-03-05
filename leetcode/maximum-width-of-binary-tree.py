# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mxm = 0
        dct = defaultdict(list)

        def maximum(node,row, col):
            if not node:
                return
            
            dct[row].append(col)
            
            ls = maximum(node.left,row+1, col*2)
            rs = maximum(node.right,row+1, col*2 + 1)

            return ls and rs
        maximum(root,0,0)
        for key,values in dct.items():
            mx = max(values)
            mn = min(values)
            mxm = max(mxm, abs(mx-mn)+1)

        print(dct)
        print(mxm)
        return mxm
        