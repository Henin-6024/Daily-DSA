# 20 POTD 
# Problem: 268. Missing Number
# Language :  python3
# Link: https://leetcode.com/problems/missing-number/submissions/1181038936

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i, num in enumerate(nums):
            ans = ans ^ (i ^ num)
        return ans
        
