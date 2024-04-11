# 11 POTD 
# Problem: 402. Remove K Digits
# Language :  python3 
# Link: https://leetcode.com/problems/remove-k-digits/submissions/1229354863
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        ans = []
        stack = []
        for i, digit in enumerate(num):
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        for _ in range(k):
            stack.pop()
        for c in stack:
            if c== '0' and not ans:
                continue
            ans.append(c)
        return ''.join(ans) if ans else '0'
