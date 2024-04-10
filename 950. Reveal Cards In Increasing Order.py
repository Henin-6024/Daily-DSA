# 26 POTD 
# Problem: 950. Reveal Cards In Increasing Order
# Language :  python3 
# Link: https://leetcode.com/problems/reveal-cards-in-increasing-order/submissions/1228596498

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        dq = collections.deque()
        for card in reversed(sorted(deck)):
            dq.rotate()
            dq.appendleft(card)
        return list(dq)
        
