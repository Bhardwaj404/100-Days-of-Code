# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        l=[]
        def dfs(node):
            if not node:
                return
            l.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
       
        dfs(root1)
        dfs(root2)
        l.sort()
        return l
