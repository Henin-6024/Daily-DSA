
# 19 POTD 
# Problem: 931. Minimum Falling Path Sum
# Language :  python 
#link: https://leetcode.com/problems/minimum-falling-path-sum/submissions/1150597669?envType=daily-question&envId=2024-01-19

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        size = len(matrix)
        prev_row_min = [0] * size
        for row in matrix:
            current_row_min = [0] * size
            for index, value in enumerate(row):
                left_bound = max(0, index-1)
                right_bound = min(size, index+2)  
                current_row_min[index] = min(prev_row_min[left_bound:right_bound]) + value
            prev_row_min = current_row_min
        return min(prev_row_min)    
