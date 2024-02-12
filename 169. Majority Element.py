# 12 POTD 
# Problem: 169. Majority Element
# Language :  python3
# Link: https://leetcode.com/problems/majority-element/submissions/1173319040

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = None
        for num in nums:
            if count == 0:
                ans = num
                count += 1
            elif ans == num:
                count += 1
            else:
                count -= 1
        return ans
        
