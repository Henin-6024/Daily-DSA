# 28 POTD 
# Problem: 1074. Number of Submatrices That Sum to Target
# Language :  python3
#link: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/submissions/1159076304?envType=daily-question&envId=2024-01-28
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
        for baseCol in range(n):
            for j in range(baseCol, n):
                prefixCount = collections.Counter({0: 1})
                sum = 0
                for i in range(m):
                    if baseCol > 0:
                        sum -= matrix[i][baseCol - 1]
                    sum += matrix[i][j]
                    ans += prefixCount[sum - target]
                    prefixCount[sum] += 1
        return ans 

