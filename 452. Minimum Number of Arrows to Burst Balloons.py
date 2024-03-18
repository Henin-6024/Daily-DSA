# 18 POTD 
# Problem: 452. Minimum Number of Arrows to Burst Balloons
# Language :  python3 
# Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1207199183

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        arrow = -math.inf
        for point in sorted(points, key = lambda x:x[1]):
            if point[0] > arrow:
                ans += 1
                arrow = point[1]
        return ans
