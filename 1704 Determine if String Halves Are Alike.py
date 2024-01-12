# 12 POTD 
# Problem: 1704. Determine if String Halves Are Alike
# Language :  python 
# link: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1144464427?envType=daily-question&envId=2024-01-12


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        kVowels = 'aeiouAEIOU'
        aVowelsCount = sum(c in kVowels for c in s[:len(s) // 2])
        bVowelsCount = sum(c in kVowels for c in s[len(s) // 2:])
        return aVowelsCount == bVowelsCount
