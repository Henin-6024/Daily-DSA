# 23 POTD 
# Problem: 1239. Maximum Length of a Concatenated String with Unique Characters
# Language :  python 
#link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/submissions/1154217844?envType=daily-question&envId=2024-01-23

class Solution:
    def maxLength(self, arr: List[str]) -> int:   
        max_length = 0  
        masks = [0] 
        for string in arr:
            mask = 0 
            for char in string:
                char_index = ord(char) - ord('a')   
                if mask >> char_index & 1:
                    mask = 0
                    break
                mask |= 1 << char_index
          
            if mask != 0:
                for existing_mask in masks.copy():
                    if existing_mask & mask == 0:
                        new_mask = existing_mask | mask  
                        masks.append(new_mask) 
                        max_length = max(max_length, bin(new_mask).count('1'))
                      
        return max_length 
        
