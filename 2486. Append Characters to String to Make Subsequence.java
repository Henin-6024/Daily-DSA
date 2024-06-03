/*
# 03 POTD 
# Problem: 2486. Append Characters to String to Make Subsequence
# Language: Java 
# Link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/submissions/1276547567
*/
class Solution {
    public int appendCharacters(String s, String t) {
        int i = 0;
        for (final char c : s.toCharArray()) {
            if (c == t.charAt(i))
                if(++i == t.length()) 
                    return 0;
        }    
        return t.length() - i;
    }
}
