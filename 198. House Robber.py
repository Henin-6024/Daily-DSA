# 21 POTD 
# Problem: 198. House Robber
# Language :  python 
#link: https://leetcode.com/problems/house-robber/submissions/1152283083?envType=daily-question&envId=2024-01-21



class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob = 0
        prev_no_rob = 0
        for num in nums:
            dp = max(prev_rob, prev_no_rob + num)
            prev_no_rob = prev_rob
            prev_rob = dp
        return prev_rob
