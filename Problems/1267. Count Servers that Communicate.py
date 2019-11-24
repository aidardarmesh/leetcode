from typing import *

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servers = set()
        
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    row.append((i,j))
            if len(row) > 1:
                for server in row:
                    servers.add(server)
        
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    col.append((i,j))
            if len(col) > 1:
                for server in col:
                    servers.add(server)
        
        return len(servers)
