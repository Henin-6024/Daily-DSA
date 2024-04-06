# 06 POTD 
# Problem: 1249. Minimum Remove to Make Valid Parentheses
# Language :  python3 
# Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/1224749017

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        chars = [c for c in s]
        for i, c in enumerate(chars):
            if c == '(':
                stack.append(i)
            elif c == ')'
                if stack:
                    stack.pop()
                else:
                    chars[i] = '*'
        while stack:
            chars[stack.pop()] = '*'
        
