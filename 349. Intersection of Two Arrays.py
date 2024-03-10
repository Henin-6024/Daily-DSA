# 10 POTD
# Problem: 349. Intersection of Two Arrays
# Language :  python3 
# Link: https://leetcode.com/problems/intersection-of-two-arrays/submissions/1199163088

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                ans.append(num)
                nums1.remove(num)
        return ans
