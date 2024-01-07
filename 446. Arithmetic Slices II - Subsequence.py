# 7 POTD 
# Problem: 446. Arithmetic Slices II - Subsequence 
# Language :  python 
#link: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/submissions/1139506328

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        dp = [collections.defaultdict(int) for i in xrange(len(nums))]
        for i in range(1, len(nums)):
            for j in xrange(i):
                diff = nums[i]-nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result 
        
