# 3 POTD 
# Problem: 2402. Meeting Rooms III
# Language:  python3
# link: https://leetcode.com/problems/meeting-rooms-iii/submissions/1178883224

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n
        meetings.sort()
        occupied = []
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                heapq.heappush(available_rooms, heapq.heappop(occupied)[1])
            if available_rooms:
                roomid = heapq.heappop(available_rooms)
                count[roomid] += 1
                heapq.heappush(occupied, (end, roomid))
            else:
                new_start, roomid = heapq.heappop(occupied)
                count[roomid] += 1
                heapq.heappush(occupied, (new_start + (end - start), roomid))
        return count.index(max(count))
