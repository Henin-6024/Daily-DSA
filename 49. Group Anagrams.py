# 6 POTD 
# Problem: 49. Group Anagrams
# Language :  python 
# link: https://leetcode.com/problems/group-anagrams/submissions/1167993937

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for str in strs:
            k = ''.join(sorted(str))
            dict[k].append(str)
        return dict.values()
