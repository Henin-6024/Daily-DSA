# 4 POTD 
# Problem: 2870. Minimum Number of Operations to Make Array Empty
# Language :  python 
#link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/submissions/1136192911

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for c in count.values():
            if c == 1:
                return -1
            ans += (c+2) // 3
        return ans
