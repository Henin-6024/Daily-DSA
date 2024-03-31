# 31 POTD 
# Problem: 2444. Count Subarrays With Fixed Bounds
# Language :  python3 
# Link: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/submissions/1219313225

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        j = -1
        prevMinKIndex = -1
        prevMaxKIndex = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                j = i
            if num == minK:
                prevMinKIndex = i
            if num == maxK:
                prevMaxKIndex = i
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)
        return ans
