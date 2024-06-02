# 02 POTD 
# Problem: 344. Reverse String
# Language: Java 
# Link:  https://leetcode.com/problems/reverse-string/submissions/1275289447

class Solution {
    public void reverseString(char[] s) {
        int l = 0;
        int r = s.length - 1;
        while (l < r ) {
            char temp = s[l];
            s[l++] = s[r];
            s[r--] = temp;
        }    
    }
}
