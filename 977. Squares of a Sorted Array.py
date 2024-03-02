# 02 POTD 
# Problem: 977. Squares of a Sorted Array
# Language:  python3 
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1191522971

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                result.append(nums[l] * nums[l])
                l += 1
            else:
                result.append(nums[r] * nums[r])
                r -= 1
        return result[::-1]
