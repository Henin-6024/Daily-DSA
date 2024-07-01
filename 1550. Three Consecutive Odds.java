/*
#01 POTD 
# Problem: 1550. Three Consecutive Odds
# Language : Java 
# Link: https://leetcode.com/problems/three-consecutive-odds/submissions/1305449652 
*/
class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int count = 0;
        for (final int a : arr) {
            count = a % 2 == 1 ? count + 1 : 0;
            if (count == 3)
                return true;
        }    
        return false;
    }
}
