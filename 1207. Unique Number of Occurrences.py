
# 17 POTD 
# Problem: 
# Language : 1207. Unique Number of Occurrences
# link: https://leetcode.com/problems/unique-number-of-occurrences/submissions/1148371800

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        element_count = Counter(arr)
        unique_occurences = set(element_count.values())
        return len(unique_occurences) == len(element_count)
        
        
