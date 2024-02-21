
# 21 POTD 
# Problem: 201. Bitwise AND of Numbers Range
# Language:  python3
# link: https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/1182164333
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right: 
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
