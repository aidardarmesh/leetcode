from typing import *

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        for from_, to in connections:
            graph[from_].append(to)
            graph[to].append(from_)
        
        res = []
        
        def bridge_util(v):
            visited.add(v)
            disc[v] = self.time
            low[v] = self.time
            self.time += 1

            for to in graph[v]:
                if not to in visited:
                    parent[to] = v

                    bridge_util(to)

                    low[v] = min(low[v], low[to])

                    if low[to] > disc[v]:
                        res.append([v,to])
                elif to != parent[v]:
                    low[v] = min(low[v], disc[to])
        
        visited = set()
        disc = [float('inf')]*n
        low = [float('inf')]*n
        parent = [-1]*n
        self.time = 0

        for v in range(n):
            if not v in visited:
                bridge_util(v)
        
        return res
        
s = Solution()
print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
