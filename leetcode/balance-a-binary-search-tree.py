# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def split(node):
            if not node:
                return
            if node:
                arr.append(node.val)
            split(node.left)
            split(node.right)
        split(root)
        arr.sort()
        def build(l,r):
            if l>r:
                return
            mid = (l+r)//2
            left = build(l,mid-1)
            right = build(mid+1,r)
            return TreeNode(arr[mid],left,right)
        print(arr)
        return build(0,len(arr)-1)
        