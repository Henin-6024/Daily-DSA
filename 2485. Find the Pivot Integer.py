# 13 POTD 
# Problem: 2485. Find the Pivot Integer
# Language :  python3 
# Link: https://leetcode.com/problems/find-the-pivot-integer/submissions/1202520936

class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        x = int(sqrt(s))
        return x if x * x == s else -1
