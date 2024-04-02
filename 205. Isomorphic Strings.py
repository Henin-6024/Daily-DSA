# 02 POTD 
# Problem: 205. Isomorphic Strings
# Language :  python3 
# Link: https://leetcode.com/problems/isomorphic-strings/submissions/1221253609

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]
