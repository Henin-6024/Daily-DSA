# 15 POTD 
# Problem: 238. Product of Array Except Self
# Language :  python3 
# Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1204601135


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * right_product
            right_product = right_product * nums[i]
        return ans
