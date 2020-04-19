from typing import *

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        uf = {i:i for i in range(1, N+1)}
        connections.sort(key=lambda x: x[2])
        total = 0
        
        def find_set(v):
            if v == uf[v]:
                return v
            
            uf[v] = find_set(uf[v])
            
            return uf[v]
        
        from collections import defaultdict, deque
        
        graph = {i:[] for i in range(1,N+1)}
        visited = {i:False for i in range(1,N+1)}
        
        for u, v, cost in connections:
            u_root = find_set(u)
            v_root = find_set(v)
            
            if u_root != v_root:
                uf[v_root] = u_root
                graph[u].append(v)
                graph[v].append(u)
                total += cost
                
        def conn_comp_num(graph):
            cnt = 0
            
            for v in graph:
                if not visited[v]:
                    deq = deque([v])
                    cnt += 1

                    while deq:
                        node = deq.popleft()

                        for to in graph[node]:
                            if not visited[to]:
                                visited[to] = True
                                deq.append(to)
            
            return cnt
        
        if conn_comp_num(graph) != 1:
            total = -1
        
        return total
