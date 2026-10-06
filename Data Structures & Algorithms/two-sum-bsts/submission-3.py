# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        _map = set()

        def inorder(root):
            if not root:
                return None

            inorder(root.left)
            _map.add(root.val)
            inorder(root.right)

        inorder(root1)

        print("_map", _map)

        ans = False 
        def inorder(root) -> bool:
            nonlocal ans

            if not root:
                return False 

            inorder(root.left)
            if root:
                # print("root.val", root.val)
                diff = target - root.val
                # print("diff", diff)

                if diff in _map:
                    # print("check", check)
                    ans = True 

            inorder(root.right)
        
        inorder(root2)
        return ans 
