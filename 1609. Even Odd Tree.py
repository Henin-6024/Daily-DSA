# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        q = deque([root])
        while  q:
            prev_val = 0 if level % 2 == 0 else float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                if level % 2 == 0 and (node.val % 2 == 0 or prev_val >= node.val):
                    return False
                if level % 2 == 1 and (node.val % 2 == 1 or prev_val <= node.val):
                    return False
                prev_val = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return True
