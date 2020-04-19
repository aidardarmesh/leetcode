from typing import *

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        visited = {i:False for i in range(N)}
        graph = {i:set() for i in range(N)}
        circles = 0
        
        for i in range(N):
            for j in range(N):
                if M[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        def dfs(v):
            if visited[v]:
                return
            
            visited[v] = True
            
            for to in graph[v]:
                if not visited[to]:
                    dfs(to)
        
        for v in graph:
            if not visited[v]:
                dfs(v)
                circles += 1
        
        return circles
