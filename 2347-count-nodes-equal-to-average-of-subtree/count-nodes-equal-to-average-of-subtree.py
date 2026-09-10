# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.r=0
        def traverse(i):
            if not i:
                return 0, 0
            ls, lc = traverse(i.left)
            rs, rc = traverse(i.right)
            cs = i.val + ls + rs
            c = 1 + lc + rc
            if cs // c == i.val:
                self.r += 1
            return cs, c
        traverse(root)
        return self.r