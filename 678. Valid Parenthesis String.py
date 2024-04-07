
# 07 POTD 
# Problem: 678. Valid Parenthesis String
# Language:  python3 
# Link: https://leetcode.com/problems/valid-parenthesis-string/submissions/1225945886


class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                if low > 0:
                    low -=1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False
        return low == 0
