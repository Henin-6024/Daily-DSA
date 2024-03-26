# 26 POTD 
# Problem: 41. First Missing Positive
# Language :  python3 
# Link: https://leetcode.com/problems/first-missing-positive/submissions/1214391201

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i , num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return n + 1
