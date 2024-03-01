# 01 POTD 
# Problem: 2864. Maximum Odd Binary Number
# Language :  python3 
# Link: https://leetcode.com/problems/maximum-odd-binary-number/submissions/1190285639

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = 0
        for i in range(len(s)):
            if s[i] == "1": count_one += 1
        ans = ""
        for i in range(count_one - 1):
            ans = ans + "1"
        for i in range(len(s) - count_one):
            ans = ans + "0"
        return ans + "1"







