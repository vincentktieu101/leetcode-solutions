# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder - node, left, right
        inorder - left, node, right
        
        [3,9,20,15,7]
        [9,3,15,20,7]
        """
        if not preorder: return None
        
        value = preorder[0]
        node = TreeNode(value)
        index = inorder.index(value)
        
        node.left = self.buildTree(preorder[1: 1 + index], inorder[:index])
        node.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])
        
        return node