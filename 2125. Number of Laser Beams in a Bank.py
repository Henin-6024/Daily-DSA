# 3 POTD 
# Problem: 2125 Number of Laser Beams in a Bank 
# Language :  python 
#link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/submissions/1135625257?envType=daily-question&envId=2024-01-03

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prevOnes = 0
        for row in bank:
            ones = row.count('1')
            if ones:
                ans += prevOnes * ones
                prevOnes = ones
            
        return ans 

