# 17 POTD 
# Problem: 1642. Furthest Building You Can Reach
# Language:  python3
# link: https://leetcode.com/problems/furthest-building-you-can-reach/submissions/1178115777

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for i in range(len(heights)-1):
            ht = heights[i]
            next_ht = heights[i + 1]
            ht_diff = next_ht - ht

            if ht_diff > 0:
                heappush(minHeap, ht_diff)
                if len(minHeap) > ladders:
                    bricks -= heappop(minHeap)
                    if bricks < 0:
                        return i
        
        return len(heights) - 1
