# 18 POTD 
# Problem: 70. Climbing Stairs
# Language :  python 
# link: https://leetcode.com/problems/climbing-stairs/submissions/1149348601

class Solution:
    def climbStairs(self, n: int) -> int:
        prev_step, cur_step = 0,1
        for _ in range(n):
            prev_step, cur_step = cur_step, prev_step + cur_step

        return cur_step
