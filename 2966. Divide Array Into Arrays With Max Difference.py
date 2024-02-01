# 1 POTD 
# Problem: 2966. Divide Array Into Arrays With Max Difference
# Language :  python 
# link : https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/submissions/1162544090?envType=daily-question&envId=2024-02-01

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return []
            answer.append([nums[i - 2], nums[i - 1], nums[i]])
            
        return answer
        
