/*
# 10 POTD 
# Problem: 1051. Height Checker
# Language: Java 
# Link: https://leetcode.com/problems/height-checker/submissions/1284111265
*/
class Solution {
    public int heightChecker(int[] heights) {
        int ans = 0;
        int currentHeight = 1;
        int [] count = new int[101];
        for (int height : heights) {
            ++count[height];
        }    
        for (int height : heights) {
            while (count[currentHeight] == 0)
                ++currentHeight;
            if (height != currentHeight) 
                ++ans;
            --count[currentHeight];
        }
        return ans;
    }
}
