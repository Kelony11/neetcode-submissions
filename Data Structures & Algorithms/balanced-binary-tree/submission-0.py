# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return [True, 0]

            l_height, l_nodes   = dfs(node.left)
            r_height, r_nodes = dfs(node.right)

            balanced = l_height and r_height and abs(l_nodes - r_nodes) <= 1

            return [balanced, 1 + max(l_nodes, r_nodes)]

        return dfs(root)[0]
        