# 13 POTD  
# Problem: 2108. Find First Palindromic String in the Array 
# Language :  python3  
# Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/submissions/1173776906

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

        
