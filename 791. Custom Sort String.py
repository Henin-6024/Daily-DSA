# 11 POTD 
# Problem: 791. Custom Sort String
# Language :  python3 
# Link: https://leetcode.com/problems/custom-sort-string/submissions/1200094371

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = Counter(s)
        sorted_chars = []
        for char in order:
            sorted_chars.append(char * char_count[char])
            char_count[char] = 0
        for char, count in char_count.items():
            sorted_chars.append(char * count)
        return ''.join(sorted_chars)
