# 29 POTD 
# Problem: 513. Find Bottom Left Tree Value
# Language :  python3 
# Link: https://leetcode.com/problems/find-bottom-left-tree-value/submissions/1189754841

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
        return node.val
        
