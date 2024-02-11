# 11 POTD 
# Problem: 1463. Cherry Pickup II
# Language :  python3
# Link: https://leetcode.com/problems/cherry-pickup-ii/submissions/1172414716

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1] * cols for _ in range(cols)]
        temp_dp = [[-1] * cols for _ in range(cols)]
        dp[0][cols - 1] = grid[0][0] + grid[0][cols - 1]
        for row in range(1, rows):
            for j1 in range(cols):
                for j2 in range(cols):
                    collected_cherries = grid[row][j1] + (0 if j1 == j2 else grid[row][j2])
                    for y1 in range(max(j1 - 1, 0), min(j1 + 2, cols)):
                        for y2 in range(max(j2 - 1, 0), min(j2 + 2, cols)):
                            if dp[y1][y2] != -1:
                                temp_dp[j1][j2] = max(temp_dp[j1][j2], dp[y1][y2] + collected_cherries)
            dp, temp_dp = temp_dp, [[-1] * cols for _ in range(cols)]
        return max(dp[j1][j2] for j1, j2 in product(range(cols), range(cols)))               

