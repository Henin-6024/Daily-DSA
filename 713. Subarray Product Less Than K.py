
# 27 POTD 
# Problem: 713. Subarray Product Less Than K
# Language :  python3 
# Link: https://leetcode.com/problems/subarray-product-less-than-k/submissions/1215634779


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        product = 1
        j = 0
        for i, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[j]
                j += 1
            ans += i - j + 1
        return ans
