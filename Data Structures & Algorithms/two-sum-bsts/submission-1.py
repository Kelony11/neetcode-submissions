# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        nums = []

        _map = set()

        def inorder(root):
            if not root:
                return None

            inorder(root.left)
            _map.add(root.val)
            inorder(root.right)

        inorder(root1)


        def inorder(root):
            if not root:
                return None 

            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        inorder(root2)

        print("nums", nums)

        for i in nums:
            diff = target - i

            if diff in _map:
                return True

            _map.add(i)

        return False

        

        # def inorder(root):
        #     if not root:
        #         return False

        #     inorder(root.left)
        #     if root:
        #         diff = target - root.val
        #         if diff in _set:
        #             return True

        #     inorder(root.right)

        # return inorder(root2)

        # return False 

        