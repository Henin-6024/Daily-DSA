# 04 POTD 
# Problem: 1614. Maximum Nesting Depth of the Parentheses
# Language :  python3 
# Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/1223254043

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        opened = 0
        for c in s:
            if c == '(':
                opened += 1
                ans =max(ans, opened)
            elif c== ')':
                opened -= 1
        return ans
