# 8 POTD 
# Problem: 938. Range Sum of BST
# Language :  python 
#link: https://leetcode.com/problems/range-sum-of-bst/submissions/1140103279


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if root is None:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
