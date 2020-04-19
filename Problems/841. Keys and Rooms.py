from typing import *

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        
        def dfs(v):
            if v in visited:
                return
            
            visited[v] = True
            
            for to in rooms[v]:
                if not to in visited:
                    dfs(to)
        
        dfs(0)
        
        return len(rooms) == len(visited)
