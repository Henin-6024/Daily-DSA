# 7 POTD 
# Problem: 451. Sort Characters By Frequency
# Language :  python 
# link: https://leetcode.com/problems/sort-characters-by-frequency/submissions/1168888668


class Solution:
    def frequencySort(self, s: str) -> str:
        freq_count = Counter(s)
        sorted_chars = sorted(freq_count.items(), key = lambda item: -item[1])
        freq_sorted_string = ''.join(character * frequency for character, frequency in sorted_chars)
        return freq_sorted_string

        
