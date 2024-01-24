# 24 POTD 
# Problem: 1457. Pseudo-Palindromic Paths in a Binary Tree.
# Language :  python3 
#link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/submissions/1155659342?envType=daily-question&envId=2024-01-24



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:  
                return
            nonlocal palindrome_path_count, value_counter
            value_counter[node.val] += 1
            if node.left is None and node.right is None:
                odd_count = sum(1 for i in range(1, 10) if value_counter[i] % 2 == 1)
               
                if odd_count < 2:
                    palindrome_path_count += 1
            else:
                dfs(node.left)
                dfs(node.right)

            value_counter[node.val] -= 1

        palindrome_path_count = 0
        value_counter = [0] * 10
       
        dfs(root)
        return palindrome_path_count
