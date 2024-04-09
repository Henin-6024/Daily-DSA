# 09 POTD 
# Problem: 2073. Time Needed to Buy Tickets
# Language:  python3 
# Link: https://leetcode.com/problems/time-needed-to-buy-tickets/submissions/1227792060

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                ans += min(ticket, tickets[k])
            else:
                ans += min(ticket, tickets[k] - 1)
        return ans
