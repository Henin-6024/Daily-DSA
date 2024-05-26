/*
# 26 POTD 
# Problem: 552. Student Attendance Record II
# Language :  Java 
# Link: https://leetcode.com/problems/student-attendance-record-ii/submissions/1268582975
*/
class Solution {
    public int checkRecord(int n) {
        final int kMod = 1_000_000_007;
        long[][] dp = new long[2][3];
        dp[0][0] = 1;
        while (n-- > 0) {
            long[][] prev = Arrays.stream(dp).map((long[] A) -> A.clone()).toArray((int length) -> new long[length][]);
            dp[0][0] = (prev[0][0] + prev[0][1] + prev[0][2]) % kMod;
            dp[0][1] = prev[0][0];
            dp[0][2] = prev[0][1];
            dp[1][0] = (prev[0][0] + prev[0][1] + prev[0][2] + prev[1][0] + prev[1][1] + prev[1][2]) % kMod;
            dp[1][1] = prev[1][0];
            dp[1][2] = prev[1][1];
        }
        return (int) ((dp[0][0] + dp[0][1] + dp[0][2] + dp[1][0] + dp[1][1] + dp[1][2]) % kMod);
    }
}
