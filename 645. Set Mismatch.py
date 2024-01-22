# 11 POTD 
# Problem: 645. Set Mismatch
# Language :  python 
#link: https://leetcode.com/problems/set-mismatch/submissions/1153192460?envType=daily-question&envId=2024-01-22

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        
        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i+1]
