# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        dec = deque([root])

        def zig(nd):
            if not nd:
                return []
            
            while dec:
                lv = len(dec)
                cur = []
                for _ in range(lv):
                    nd = dec.popleft()
                    cur.append(nd.val)

                    if nd.left:
                        dec.append(nd.left)
                    
                    if nd.right:
                        dec.append(nd.right)
                    
                lst.append(cur)
        zig(root)
        for i in range(len(lst)):
            if i % 2==1:
                lst[i].reverse()
        return lst
            
        