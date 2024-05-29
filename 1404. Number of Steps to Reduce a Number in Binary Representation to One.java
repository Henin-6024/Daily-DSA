/*
# 29 POTD 
# Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Language : Java 
# Link:  https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/submissions/1271652706
*/
class Solution {
    public int numSteps(String s) {
    int ans = 0;
    StringBuilder sb = new StringBuilder(s);   
    while (sb.charAt(sb.length() - 1) == '0') {
        sb.deleteCharAt(sb.length() - 1);
        ++ans;
    } 
    if (sb.toString().equals("1")) return ans;
    ++ans;
    for (final char c : sb.toString().toCharArray())
        ans += c == '1' ? 1 : 2;
    return ans;
    }
}
