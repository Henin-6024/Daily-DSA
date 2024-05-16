/**
# 16 POTD 
# Problem: 2331. Evaluate Boolean Binary Tree
# Language:  Java
# Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/submissions/1259499371


 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean evaluateTree(TreeNode root) {
        if (root.val < 2) return root.val == 1;
        if (root.val == 2) return evaluateTree(root.left) || evaluateTree(root.right);
        return evaluateTree(root.left) && evaluateTree(root.right);
        
    }
}
