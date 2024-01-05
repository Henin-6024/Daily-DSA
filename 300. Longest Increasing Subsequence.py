# 5 POTD 
# Problem: 300. Longest Increasing Subsequence
# Language :  python 
#link: https://leetcode.com/problems/longest-increasing-subsequence/submissions/1137615382


#Using DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
