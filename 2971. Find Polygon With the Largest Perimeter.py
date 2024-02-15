
# 3 POTD 
# Problem: 2971. Find Polygon With the Largest Perimeter
# Language:  python3
# link: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/submissions/1176166819

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        polygon_side = sum (nums)
        for num in sorted(nums, reverse=True):
            polygon_side -= num
            if polygon_side > num:
                return polygon_side + num
        return -1
