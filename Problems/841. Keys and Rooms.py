from typing import *

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visited = {0}
        
        while queue:
            i = queue.pop(0)
            
            for next_ in rooms[i]:
                if not next_ in visited:
                    queue.append(next_)
                    visited.add(next_)
        
        return len(visited) == len(rooms)
