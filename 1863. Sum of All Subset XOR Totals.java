/*
# 20 POTD 
# Problem:1863. Sum of All Subset XOR Totals
# Language :  Java
# Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/submissions/1263106844
*/
class Solution {
    public int subsetXORSum(int[] nums) {
        return dfs(nums, 0, 0);
    }
    private int dfs(int[] nums, int i, int xors) {
        if(i == nums.length) return xors;
        final int x = dfs(nums, i + 1 , xors);
        final int y = dfs(nums, i + 1, nums[i] ^ xors);
        return x + y;
    }
}
