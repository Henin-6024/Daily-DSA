
# 3 POTD 
# Problem: 1043. Partition Array for Maximum Sum
# Language:  python3
# link: https://leetcode.com/problems/partition-array-for-maximum-sum/submissions/1165034300

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        arr_length = len(arr)
        dp = [0] * (arr_length + 1)
        for i in range(1, arr_length + 1):
            max_element = 0
            for j in range(i, max(0, i-k), -1):
                max_element = max(max_element, arr[j-1])
                dp[i] = max(dp[i], dp[j-1] + max_element * (i - j + 1))
        return dp[arr_length]
