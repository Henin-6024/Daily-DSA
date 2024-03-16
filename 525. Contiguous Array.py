# 16 POTD 
# Problem: 525. Contiguous Array
# Language :  python3 
# Link: https://leetcode.com/problems/contiguous-array/submissions/1205300573

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0
        prefix_to_index = {0: -1}
        for i, num in enumerate(nums):
            prefix += 1 if num else -1
            ans = max(ans, i - prefix_to_index.setdefault(prefix, i))
        return ans
