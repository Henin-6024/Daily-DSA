
# 19 POTD 
# Problem: 621. Task Scheduler
# Language :  python3 
# Link: https://leetcode.com/problems/task-scheduler/submissions/1208432693 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0 for _ in range(26)]
        for t in tasks:
            count[ord(t) - 65] += 1
        max_num = max(count)
        m = 0
        for i in range(26):
            if count[i] == max_num:
                m += 1
        return max(len(tasks), (max_num - 1) * (n + 1) + m)
