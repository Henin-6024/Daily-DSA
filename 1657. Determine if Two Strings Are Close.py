# 14 POTD 
# Problem: 1657. Determine if Two Strings Are Close
# Language :  python 
#link: https://leetcode.com/problems/determine-if-two-strings-are-close/submissions/1149355968?envType=daily-question&envId=2024-01-14

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)
        if count1.keys() != count2.keys():
            return False
        return sorted(count1.values()) == sorted(count2.values())
  
