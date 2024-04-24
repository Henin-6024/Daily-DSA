// # 24 POTD 
// # Problem: 1137. N-th Tribonacci Number
// # Language :  Java
// # Link: https://leetcode.com/problems/n-th-tribonacci-number/submissions/1241020661

class Solution {
    public int tribonacci(int n) {
        int [] dp = {0, 1, 1};
        for (int i = 3; i<= n; ++i) dp[i % 3] = dp[0] + dp[1] + dp[2];
        return dp[n % 3];
    }
}
