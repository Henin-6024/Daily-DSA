# 25 POTD 
# Problem: 442. Find All Duplicates in an Array
# Language :  python3 
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1213705840

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            nums[abs(num) - 1] *= -1
            if nums[abs(num) - 1] > 0:
                ans.append(abs(num))
        return ans
