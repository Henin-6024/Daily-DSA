
# 3 POTD 
# Problem: 76. Minimum Window Substring
# Language:  python3
# link: https://leetcode.com/problems/minimum-window-substring/submissions/1165843489
class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        count = collections.Counter(t)
        required = len(t)
        Left = -1
        minLength = len(s) + 1

        l = 0
        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            while required == 0:
                if r - l + 1 < minLength:
                    Left = l
                    minLength = r - l + 1
                count[s[l]] += 1
                if count[s[l]] > 0:
                    required += 1
                l += 1

        return '' if Left == -1 else s[Left: Left + minLength]



        
