# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def max_deep(node):
            if not node:
                return 0
            return 1+max(max_deep(node.left),max_deep(node.right))
        def sumatdepth(node,current,target):
            if not node:
                return 0
            if current==target:
                return node.val
            left=sumatdepth(node.left,current+1,target)
            right=sumatdepth(node.right,current+1,target)
            return left+right
        depth=max_deep(root)
        return sumatdepth(root,1,depth)