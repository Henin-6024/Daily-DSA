# 29 POTD 
# Problem: 2997. Minimum Number of Operations to Make Array XOR Equal to K
# Language :  python3 
# Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/submissions/1245096327

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    return functools.reduce(operator.xor, nums, k).bit_count() 
