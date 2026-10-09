# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def GetMinNode(self, node) -> Optional[TreeNode]:

        curr = node
        # print("curr", curr)

        if curr and curr.left:
            return self.GetMinNode(curr.left)
        
        # print("curr", curr, "curr.val", curr.val)
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        # Search for the node 
        if not root:
            return root

        # print("root.val", root.val, "key", key)
        if root.val < key:
            # print("RIGHT")
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            # print("LEFT")
            root.left = self.deleteNode(root.left, key)
        else:
            # print("FOUND")
            # found the key

            # CASE 1: the key node has 0 or 1 children

            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left

            # CASE 2: the key node has 2 children
            else:
                min_node = self.GetMinNode(root.right)
                # print("min_node.val", min_node.val)
                # replace the key node with the min from the right sub tree

                root.val = min_node.val 
                # print("root.val", root.val)

                # find the node the min node is located and delete it
                root.right = self.deleteNode(root.right, min_node.val)
                # print("root.right", root.right)

        return root



        
        