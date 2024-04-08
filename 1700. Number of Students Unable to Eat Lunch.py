# 08 POTD 
# Problem: 1700. Number of Students Unable to Eat Lunch
# Language:  python3 
# Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/1226812027

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        for i, sandwich in enumerate(sandwiches):
            if count[sandwich] == 0:
                return len(sandwiches) - i
            count[sandwich] -= 1
        return 0
