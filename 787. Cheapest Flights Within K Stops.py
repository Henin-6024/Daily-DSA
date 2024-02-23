
# 23 POTD 
# Problem: 787. Cheapest Flights Within K Stops
# Language :  python3 
#link: https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/1184109945

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        infinite = float('inf')
      
        distance = [infinite] * n
        distance[src] = 0

        for _ in range(k + 1):
            distance_backup = distance.copy()

            for from_node, to_node, price in flights:
                distance[to_node] = min(distance[to_node], distance_backup[from_node] + price)

        return -1 if distance[dst] == infinite else distance[dst]
