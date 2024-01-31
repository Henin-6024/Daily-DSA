# 31 POTD 
# Problem: 739. Daily Temperatures
# Language :  python3
# link: https://leetcode.com/problems/daily-temperatures/submissions/1161591146?envType=daily-question&envId=2024-01-31

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
      
        for index, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                prev_index = stack.pop()
                ans[prev_index] = index - prev_index
          
            stack.append(index)
      
        return ans
