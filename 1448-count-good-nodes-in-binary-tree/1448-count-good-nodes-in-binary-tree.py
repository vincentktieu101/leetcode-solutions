# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(curr_max, root):
            if not root: return
            if curr_max <= root.val:
                self.ans += 1
                curr_max = root.val
            dfs(curr_max, root.left)
            dfs(curr_max, root.right)
        
        dfs(float('-inf'), root)
        
        return self.ans