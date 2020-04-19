from typing import *

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        from collections import deque
        
        N = len(M)
        visited = {i:False for i in range(N)}
        graph = {i:set() for i in range(N)}
        circles = 0
        
        for i in range(N):
            for j in range(N):
                if M[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        def bfs(v):
            deq = deque(graph[v])
            
            while deq:
                neigh = deq.popleft()
                
                for to in graph[neigh]:
                    if not visited[to]:
                        visited[to] = True
                        deq.append(to)
        
        for v in graph:
            if not visited[v]:
                bfs(v)
                circles += 1
        
        return circles
