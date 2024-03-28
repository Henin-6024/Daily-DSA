# 28 POTD 
# Problem: 2958. Length of Longest Subarray With at Most K Frequency
# Language :  python3 
# Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/submissions/1215905512

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        count = collections.Counter()
        l = 0
        for r, num in enumerate(nums):
            count[num] += 1
            while count[num] == k + 1 :
                count[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
