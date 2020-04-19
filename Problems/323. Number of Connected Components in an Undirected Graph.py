from typing import *

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        visited = {i:False for i in range(n)}
        cnt = 0
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(v):
            if visited[v]:
                return
            
            visited[v] = True
            
            for to in graph[v]:
                if not visited[to]:
                    dfs(to)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                cnt += 1
        
        return cnt
