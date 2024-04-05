# 05 POTD 
# Problem: 1544. Make The String Great
# Language:  python3 
# Link: https://leetcode.com/problems/make-the-string-great/submissions/1223651452 

class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for c in s:
            if ans and self.badPair(ans[-1], c):
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
    def badPair(self, a: str, b: str) -> bool:
        return a != b and a.lower() == b.lower()
        
