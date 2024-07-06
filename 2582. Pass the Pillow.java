/*
# 06 POTD  
# Problem: 2582. Pass the Pillow 
# Language: Java  
# Link: https://leetcode.com/problems/pass-the-pillow/submissions/1311954287
*/
class Solution {
    public int passThePillow(int n, int time) {
        time %= (n - 1) * 2;
        if (time < n) 
            return 1 + time;
        return n - (time - (n - 1));
    }
}
