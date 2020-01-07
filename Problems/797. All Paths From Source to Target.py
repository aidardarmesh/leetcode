from typing import *

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph)-1
        ans = []
        
        def dfs(v, path):
            if v == dest:
                ans.append(path)
            
            for to in graph[v]:
                dfs(to, path[:] + [to])
        
        dfs(0, [0])
        
        return ans
