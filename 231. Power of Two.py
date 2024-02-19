# 19 POTD 
# Problem: 1207. Unique Number of Occurrences
# Language : Python3
# link: https://leetcode.com/problems/power-of-two/submissions/1180101003

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while (n != 1):
            if (n %2 != 0):
                return False
            n =  n // 2 
        return True   
