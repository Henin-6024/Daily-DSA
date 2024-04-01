# 01 POTD 
# Problem: 58. Length of Last Word
# Language:  python3 
# Link: https://leetcode.com/problems/length-of-last-word/submissions/1219914104


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        lastIndex = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        return lastIndex - i
