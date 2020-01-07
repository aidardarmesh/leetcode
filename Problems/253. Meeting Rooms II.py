from typing import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        
        intervals.sort(key=lambda x: x[0])
        rooms = []
        
        for s, e in intervals:
            # current interval can replace soon ending meeting
            # no additional room required
            if rooms and s >= rooms[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, e)
            else:
                heapq.heappush(rooms, e)
        
        return len(rooms)
