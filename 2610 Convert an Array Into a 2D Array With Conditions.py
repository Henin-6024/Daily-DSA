#Leetcode series: day 3
#2610: Convert an Array Into a 2D Array With Conditions
#Language: python
#link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/submissions/1134736524?envType=daily-question&envId=2024-01-02


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        ans = []
        for x, v in cnt.items():
            for i in range(v):
                if len(ans) <= i:
                    ans.append([])
                ans[i].append(x)
        return ans
