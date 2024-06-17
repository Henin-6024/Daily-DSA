/*
# 17 POTD 
# Problem: 633. Sum of Square Numbers
# Language: Java
# Link: https://leetcode.com/problems/sum-of-square-numbers/submissions/1291447809
*/
class Solution {
    public boolean judgeSquareSum(int c) {
        long s = 0;
        long l = (long) Math.sqrt(c);
        while (s <= l) {
            long sum = s * s + l * l;
            if (sum == c) 
                return true;
            if (sum < c) 
                ++s;
            else 
                --l;
        }
        
    return false;
    }
}
