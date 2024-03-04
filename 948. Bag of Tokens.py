# 04 POTD 
# Problem: 948. Bag of Tokens
# Language :  python3 
# Link: https://leetcode.com/problems/bag-of-tokens/submissions/1193589024?envType=daily-question&envId=2024-03-04

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        ans, score = 0, 0
        while left <= right:
            if power >= tokens[left]:
                score, power, left = score + 1, power - tokens[left], left +1
                
            elif score > 0:
                score, power, right = score - 1, power + tokens[right], right - 1
            else: 
                break
            ans = max(ans, score)
        return ans
