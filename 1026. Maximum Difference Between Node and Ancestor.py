# 11 POTD 
# Problem: 1026. Maximum Difference Between Node and Ancestor
# Language :  python 
#link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/1143524192
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: [TreeNode]) -> int:
        def dfs(root, max_val, min_val):
            tmp = max(abs(root.val - max_val), abs(root.val - min_val))
            self.res = max(self.res, tmp)
            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            if root.left:
                dfs(root.left, max_val, min_val)
            if root.right:
                dfs(root.right, max_val, min_val)
        self.res = 0
        dfs(root, root.val, root.val)
        return self.res
