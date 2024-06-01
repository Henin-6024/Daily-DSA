/*
# 01 POTD 
# Problem: 3110. Score of a String
# Language :  Java 
# Link: https://leetcode.com/problems/score-of-a-string/submissions/1274325634
*/
class Solution {
    public int scoreOfString(String s) {
        int ans = 0;
        for (int i = 1; i < s.length(); ++i) {
            ans += Math.abs(s.charAt(i) - s.charAt(i - 1));
        }    
        return ans;
    }
}
