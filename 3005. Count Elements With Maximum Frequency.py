# 08 POTD 
# Problem: 3005. Count Elements With Maximum Frequency
# Language :  python3 
# Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/submissions/1197730471

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        maxFrequency = max(count.values())
        return sum(frequency == maxFrequency for frequency in count.values()) * maxFrequency
