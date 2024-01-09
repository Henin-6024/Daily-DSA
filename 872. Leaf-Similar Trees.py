# 9 POTD 
# Problem: 872. Leaf-Similar Trees
# Language :  python3 
#link: https://leetcode.com/problems/leaf-similar-trees/submissions/1141017157



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def findLeaf(root, leaf_seq):
            if not root: return
            if not root.left and not root.right:
                leaf_seq.append(root.val)
            findLeaf(root.left, leaf_seq)
            findLeaf(root.right, leaf_seq)
            return leaf_seq
        root1_leaf = findLeaf(root1, [])
        root2_leaf = findLeaf(root2, [])
        return root1_leaf == root2_leaf
