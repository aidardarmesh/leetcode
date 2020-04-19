from typing import *

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        from collections import deque
        
        N = len(M)
        visited = {i:False for i in range(N)}
        circles = 0
        
        for i in range(N):
            if not visited[i]:
                deq = deque([i])
                circles += 1
                
                while deq:
                    i = deq.popleft()
                    visited[i] = True
                    
                    for j in range(N):
                        if M[i][j] and not visited[j]:
                            deq.append(j)
        
        return circles
