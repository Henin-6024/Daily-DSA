# 09 POTD 
# Problem: 2540. Minimum Common Value
# Language :  python3 
# Link: https://leetcode.com/problems/minimum-common-value/submissions/1198136199

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
