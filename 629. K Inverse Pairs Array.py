# 11 POTD 
# Problem: 629. K Inverse Pairs Array
# Language :  python 
#link: https://leetcode.com/problems/k-inverse-pairs-array/submissions/1157980157?envType=daily-question&envId=2024-01-27

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7  
       
        dp = [1] + [0] * k  
        prefix_sum = [0] * (k + 2)
        for current_number in range(1, n + 1): 
            for inverse_count in range(1, k + 1):
                dp[inverse_count] = (prefix_sum[inverse_count + 1] - prefix_sum[max(0, inverse_count - (current_number - 1))]) % mod

            for index in range(1, k + 2):
                prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod
        
        return dp[k]
        
