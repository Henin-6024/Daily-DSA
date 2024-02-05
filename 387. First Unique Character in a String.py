# 5 POTD 
# Problem: 387. First Unique Character in a String
# Language:  python3
# link: https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1166441641



class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

        
