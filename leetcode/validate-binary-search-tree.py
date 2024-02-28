# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = []
        def valn(nd):
            nonlocal lst
            if not nd:
                return 0
            valn(nd.left)
            lst.append(nd.val)
            valn(nd.right)
        valn(root)
        srt = sorted(lst)
        if srt == lst:
            for i in range(1,len(lst)):
                if lst[i] == lst[i-1]:
                    return False
            return True
        else:
            return False
        