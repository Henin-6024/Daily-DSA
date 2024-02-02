# 2 POTD 
# Problem: 
# Language: 1291. Sequential Digits
# link: https://leetcode.com/problems/sequential-digits/submissions/1163517067?envType=daily-question&envId=2024-02-02

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for starting_digit in range(1, 9):
            current_number = starting_digit
            for next_digit in range(starting_digit + 1, 10):
                current_number = current_number *10 + next_digit
                if low <= current_number <= high:
                    ans.append(current_number)
        return sorted(ans)

  
